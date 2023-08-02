from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

access_token = "dp:VjC,wp2sS1387u><A?Y~F+nk8haGDIBYQegTGnXxgrEYxLdSuuvjxHcNaRKEI"

storage = {}


@app.route("/api/v1", methods=["GET", "POST"])
def json_store():
    if not is_auth(request):
        return {"message": "Sorry."}
    if request.method == "POST":
        storage.update(request.json)
        return request.json

    return storage


@app.route("/api/v1/<path:key>", methods=["GET", "DELETE"])
def json_by_key(key=""):
    if not is_auth(request):
        return {"message": "Sorry."}

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
