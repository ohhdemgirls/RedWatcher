import settings
from flask import *
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(settings)
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
	return render_template("404.html"), 404


@app.route("/")
def index():
	from models import DATA_MODEL as cls

	limit = request.args.get("limit")
	if not limit or not limit.isdigit():
		limit = settings.WARK_DEFAULT_MAX_POSTS
	else:
		limit = int(limit)

	obj_list = cls.query.order_by(cls.timestamp.desc()).limit(limit)
	for k, v in request.args.items():
		if hasattr(cls, k) or hasattr(cls, k + "_id"):
			col = getattr(cls, k, getattr(cls, k + "_id"))
			if type(col.property._orig_columns[0].type) is type(db.Integer()):
				if not v.isdigit():
					continue
				v = int(v)
			obj_list = obj_list.filter(**{col: v})
	return render_template("index.html", obj_list=obj_list)


if __name__ == "__main__":
	import sys

	ip, port = "127.0.0.1", 5000
	if len(sys.argv) > 1:
		ip = sys.argv[1]
		if len(sys.argv) > 2:
			port = int(sys.argv[2])
	app.run(ip, port)
