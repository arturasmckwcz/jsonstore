from flask import Flask, abort, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

access_token = os.environ.get("JSONSTORE_ACCESS_TOKEN")
if not access_token:
    access_token = "any random string for auth"

storage = {}


@app.before_request
def check_auth():
    if not is_auth(request):
        abort(401)


@app.route("/api/v1", methods=["GET", "POST"])
def json_store():
    if request.method == "POST":
        storage.update(request.json)
        return request.json

    return storage


@app.route("/api/v1/<path:key>", methods=["GET", "DELETE"])
def json_by_key(key=""):
    if not key in list(storage.keys()):
        return {key: ""}

    if request.method == "GET":
        return {key: storage[key]}

    if request.method == "DELETE":
        return {key: storage.pop(key)}


def is_auth(request):
    token = request.headers.get("token")
    if token == access_token:
        return True

    return False
