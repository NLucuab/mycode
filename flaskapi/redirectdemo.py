#!/usr/bin/env python3

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

pic_location = "https://static.alta3.com/courses/api/lec_flaskcontrol_python/dont-panic.png"

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/")
def index():
    return render_template("towel.html", pic=pic_location)

@app.route("/login", methods=["POST", "GET"])
@limiter.limit("3 per day")
def login():
    if request.method == "POST":
        if request.form["answer"] == "42":
            return redirect(url_for("success"))
        else:
            return redirect(url_for("fail"))
    elif request.method == "GET":
        return redirect(url_for("index"))


@app.route("/httpfail")
def httpfail():
    abort(406)

@app.route("/fail")
def fail():
    return "That was not correct."

@app.route("/success")
def success():
    return "Correct!"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
