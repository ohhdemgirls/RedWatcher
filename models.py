from collections import namedtuple
from datetime import datetime
from app import db


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	reddit_id = db.Column(db.String(16), unique=True)
	subreddit = db.Column(db.String(205))
	title = db.Column(db.String(300))
	url = db.Column(db.String(300))
	author = db.Column(db.String(40))
	timestamp = db.Column(db.DateTime)

	@property
	def reddit_link(self):
		return "http://redd.it/%s" % (self.reddit_id)

	@classmethod
	def create_from_praw(cls, post):
		instance = cls(
			reddit_id = post.id,
			subreddit = post.subreddit.display_name,
			title = post.title,
			url = post.url,
			author = post.author.name if post.author else "",
			timestamp = datetime.fromtimestamp(post.created_utc)
		)
		db.session.add(instance)
		db.session.commit()
		return instance

DATA_MODEL = Post


if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1 and sys.argv[1] == "--setup":
		db.create_all()
		print("Work complete.")
		exit()
