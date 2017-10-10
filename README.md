RedWatcher
====

A subreddit archiver.

This code is currently broken, updates will be pushed soon.

Working Demo
====

https://giant.gfycat.com/ColorlessPeriodicBlueshark.webm


Installation
------------

Wark is a [Flask](http://flask.pocoo.org/) application, compatible with
Python 2.7+ and Python 3.2+.

Running the app in a virtualenv setup is highly recommended:
  https://virtualenv.readthedocs.org/en/latest/virtualenv.html

Flask has several production setup options. One recommended one is uWSGI:
  http://flask.pocoo.org/docs/deploying/uwsgi/

To install all dependencies, run this command from within the virtualenv:

```
pip install -r requirements.txt
```

On first run, in order to initialize the database, run the following command:
```
python models.py --setup
```

To start the scanner daemon, run `python daemon.py`.

To start the Flask development server, run `python app.py`. Do not use this in
production! Instead, set up uWSGI as described above.


Settings
--------

The `settings.py` file contains some development defaults for all settings.

A list of Flask settings and their defaults is available in the Flask docs:
  https://flask.pocoo.org/docs/config/

A list of available SQLAlchemy settings is also available:
  https://pythonhosted.org/Flask-SQLAlchemy/config.html

Wark will automatically look for a `local_settings.py` file to override all
settings with. Modifying settings in such a file is recommended.

In addition to all these, the following application settings are available:

 * `WARK_USER_AGENT`: The user agent of the scanner.
 * `WARK_SUBREDDITS`: List of subreddits to scan.
 * `WARK_MAX_CACHED_ITEMS`: List of IDs to keep in cache. Increasing this value
    reduces database load, but can increase memory usage.
 * `WARK_REQUEST_THROTTLE`: Seconds to wait between each scan of the new queue.
    Note that Reddit keeps the new queue in cache for a few minutes, so setting
    this too low is counter-productive.
 * `WARK_POSTS_PER_REQUEST`: Amount of new posts to query for every time.


Software
--------

#### Backend / Daemon:
 * [Python](https://python.org/)
 * [PRAW](https://praw.readthedocs.org)
 * [Flask](http://flask.pocoo.org)
 * [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)

#### UI:
 * [jQuery](https://jquery.org)
 * [DataTables](https://datatables.net)

#### Recommended production setup:
 * [nginx](http://nginx.org)
 * [PostgreSQL](https://www.postgresql.org)
 * [virtualenv](https://virtualenv.readthedocs.org)
