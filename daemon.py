import sys
from collections import deque
from time import sleep
from praw import Reddit
from sqlalchemy.exc import IntegrityError
from app import db
from models import Post
from settings import *


def warn(msg):
	sys.stderr.write("Warning: %s\n" % (msg))


# Cache deque to prevent hitting the db too much
_handle_cache = deque(maxlen=WARK_MAX_CACHED_ITEMS)
def handle_post(post):
	if post.id in _handle_cache:
		return

	try:
		Post.create_from_praw(post)
	except IntegrityError as e:
		warn(e)
		db.session.rollback()
	else:
		print("Saved %r (%s)" % (post.id, post))
	finally:
		_handle_cache.append(post.id)


def main():
	reddit = Reddit(user_agent=WARK_USER_AGENT)
	while True:
		for subreddit_name in WARK_SUBREDDITS:
			try:
				subreddit = reddit.get_subreddit(subreddit_name)
				posts = subreddit.get_new(limit=WARK_POSTS_PER_REQUEST)
				for post in posts:
					handle_post(post)
			except Exception as e:
				warn("Received an exception while communicating with the API: %r" % (e))
			sleep(WARK_REQUEST_THROTTLE)


if __name__ == "__main__":
	main()
