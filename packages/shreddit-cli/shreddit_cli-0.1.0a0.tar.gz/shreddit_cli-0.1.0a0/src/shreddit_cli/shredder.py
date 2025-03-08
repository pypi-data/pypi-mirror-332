import json
import logging
import os
import time
from datetime import datetime, timedelta
from re import sub

import praw
from praw.models import Comment, Submission
from prawcore.exceptions import BadRequest, OAuthException, ResponseException
from shreddit_cli.util import ShredditError, get_sentence


class Shredder(object):
    """This class stores state for configuration, API objects, logging, etc. It exposes a shred() method that
    application code can call to start it.
    """

    def __init__(self, config, user):
        logging.basicConfig()
        self._logger = logging.getLogger("shreddit")
        self._logger.setLevel(
            level=logging.DEBUG if config.get("verbose", True) else logging.INFO
        )
        self.__dict__.update({"_{}".format(k): config[k] for k in config})

        self._user = user
        self._connect()

        if self._save_directory:
            self._r.config.store_json_result = True

        self._recent_cutoff = datetime.now() - timedelta(hours=self._hours)

        if self._nuke_hours:
            self._nuke_cutoff = datetime.now() - timedelta(hours=self.nuke_hours)

        if self._save_directory:
            if not os.path.exists(self._save_directory):
                os.makedirs(self._save_directory)

        # Add any multireddit subreddits to the whitelist
        self._whitelist = set([s.lower() for s in self._whitelist])
        for username, multiname in self._multi_whitelist:
            multireddit = self._r.multireddit(username, multiname)
            for subreddit in multireddit.subreddits:
                self._whitelist.add(str(subreddit).lower())

        # Add any multireddit subreddits to the blacklist
        self._blacklist = set()
        for username, multiname in self._multi_blacklist:
            multireddit = self._r.multireddit(username, multiname)
            for subreddit in multireddit.subreddits:
                self._blacklist.add(str(subreddit).lower())

        if self._nuke_hours:
            self._logger.info(f"Deleting ALL items before {self._nuke_cutoff}")

        self._logger.info(f"Ignoring ALL items after {self._recent_cutoff}")
        self._logger.info(f"Targeting {self._item} sorted by {self._sort}")
        if self._blacklist:
            self._logger.info(
                "Deleting ALL items from subreddits {}".format(
                    ", ".join(list(self._blacklist))
                )
            )
        if self._whitelist:
            self._logger.info(f"Keeping items from subreddits {self._whitelist}")
        if self._keep_a_copy and self._save_directory:
            self._logger.info(f"Saving deleted items to: {self._save_directory}")
        if self._trial_run:
            self._logger.info("Trial run - no deletion will be performed")

    def shred(self):
        deleted = self._remove_things(self._build_iterator())
        if deleted >= self._batch_cooldown_size:
            # This user has more than X items to handle, which angers the gods of the Reddit API. So chill for a
            # while and do it again.
            self._logger.info(
                f"Waiting {self._batch_cooldown_time} seconds and continuing..."
            )
            time.sleep(self._batch_cooldown_time)
            self._connect()
            self.shred()

    def _connect(self):
        try:
            self._r = praw.Reddit(
                self._user, check_for_updates=False, user_agent="python:shreddit:v6.0.4"
            )
            self._logger.info(f"Logged in as {self._r.user.me()}")
        except ResponseException:
            raise ShredditError("Bad OAuth credentials")
        except OAuthException:
            raise ShredditError("Bad username or password")

    def _check_whitelist(self, item):
        """Returns True if the item is whitelisted, False otherwise."""
        if (
            str(item.subreddit).lower() in self._whitelist
            or item.id in self._whitelist_ids
        ):
            return "whitelisted"
        if self._whitelist_distinguished and item.distinguished:
            return "distinguished"
        if self._whitelist_gilded and item.gilded:
            return "gilded"
        if self._max_score is not None and item.score > self._max_score:
            return f"max score > {self._max_score}"
        return ""

    def _save_item(self, item):
        name = item.subreddit_name_prefixed[2:]
        path = "{}/{}/{}.json".format(item.author, name, item.id)
        if not os.path.exists(
            os.path.join(self._save_directory, os.path.dirname(path))
        ):
            os.makedirs(os.path.join(self._save_directory, os.path.dirname(path)))
        with open(os.path.join(self._save_directory, path), "w") as fh:
            # This is a temporary replacement for the old .json_dict property:
            output = {
                k: item.__dict__[k] for k in item.__dict__ if not k.startswith("_")
            }
            output["subreddit"] = output["subreddit"].title
            output["author"] = output["author"].name
            json.dump(output, fh, indent=2)

    def _remove_submission(self, sub):
        self._logger.info(f"Deleting submission: {sub.id} {sub.url}")

    def _remove_comment(self, comment):
        if self._replacement_format == "random":
            replacement_text = get_sentence()
        elif self._replacement_format == "dot":
            replacement_text = "."
        else:
            replacement_text = self._replacement_format

        short_text = sub(b"\n\r\t", " ", comment.body[:35])
        msg = "/r/{}/ #{} ({}) with: {}".format(
            comment.subreddit, comment.id, short_text, replacement_text
        )

        self._logger.debug(f"Editing and deleting {msg}")
        if not self._trial_run:
            comment.edit(replacement_text)

    def _remove(self, item):
        if self._keep_a_copy and self._save_directory:
            self._save_item(item)
        if not self._trial_run:
            if self._clear_vote:
                try:
                    item.clear_vote()
                except BadRequest:
                    self._logger.debug(f"Couldn't clear vote on {item}")
        if isinstance(item, Submission):
            self._remove_submission(item)
        elif isinstance(item, Comment):
            self._remove_comment(item)
        if not self._trial_run:
            item.delete()

    def _remove_things(self, items):
        to_delete = list(items)
        deleted = []
        self._logger.info(f"Deleting batch of {len(to_delete)} items...")

        for item in to_delete:
            self._logger.info(f"Examining item: {item} ({item.url})")
            created = datetime.fromtimestamp(item.created_utc)

            if str(item.subreddit).lower() in self._blacklist:
                self._logger.info("Deleted: on blacklist")
                deleted.append(item)
                self._remove(item)
            elif self._nuke_hours and created <= self._nuke_cutoff:
                self._logger.info("Deleted: created prior to nuke cutoff")
                deleted.append(item)
                self._remove(item)
            elif reason := self._check_whitelist(item):
                self._logger.info(f"Skipping: {reason}")
                continue
            elif created > self._recent_cutoff:
                self._logger.info("Skipping: too recent")
                continue
            else:
                deleted.append(item)
                self._remove(item)
        self._logger.info(f"Finished deleting {len(deleted)} items.")
        return len(deleted)

    def _build_iterator(self):
        item = self._r.user.me()
        if self._item == "comments":
            item = item.comments
        elif self._item == "submitted":
            item = item.submissions

        if self._sort == "new":
            return item.new(limit=None)
        elif self._sort == "top":
            return item.top(limit=None)
        elif self._sort == "hot":
            return item.hot(limit=None)
        elif self._sort == "controversial":
            return item.controversial(limit=None)
        else:
            raise ShredditError(f"Sorting {self._sort} not recognized.")
