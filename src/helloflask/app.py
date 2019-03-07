
import flask
import os
import socket


def create_app(settings=None):
    app = flask.Flask(__name__)

    mypid = os.getpid()
    myhost = socket.getfqdn()
    @app.route("/")
    def index():
        return f"hello from {app.name} on {myhost} (pid:{mypid})"

    return app
