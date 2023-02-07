import os
from lovelace import app, socketio


@app.route("/")
def index():
    return "I'm alive!"


if __name__ == "__main__":
    host = "127.0.0.1" if os.environ.get("IN_DOCKER", False) else "0.0.0.0"
    socketio.run(
        app,
        debug=False,
        host=host,
        port=3000,
        ssl_context=("ec2-cert.pem", "ec2-key.pem"),
    )
