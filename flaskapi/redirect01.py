#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("log_in.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin":
            return redirect(url_for("success"))
        else:
            abort(401)
    elif request.method == "GET":
        return redirect(url_for("index"))

@app.route("/success")
def success():
    return "logged in successfully"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
