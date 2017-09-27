# Wark settings
import os


__version__ = (0, 8, 0)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Set to False in production
DEBUG = True

# Change this in production
SECRET_KEY = "5cc536a613ff5b0a1f77d445fee4c15c38356d2461da7cc22a6ef2c6ba14d8e8"

# Database configuration
# See: http://pythonhosted.org/Flask-SQLAlchemy/config.html
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
SQLALCHEMY_ECHO = DEBUG

# Daemon settings
WARK_USER_AGENT = "Praw/WArk %s" % (".".join(str(i) for i in __version__))
WARK_SUBREDDITS=["linux"]
WARK_MAX_CACHED_ITEMS = 1000
WARK_REQUEST_THROTTLE = 30
WARK_POSTS_PER_REQUEST = 300

# Client settings
WARK_DEFAULT_MAX_POSTS = 2500

# Leave the following lines to override settings in a "local_settings.py" file
try:
	from local_settings import *
except ImportError:
	pass
