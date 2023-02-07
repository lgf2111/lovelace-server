import os
from lovelace import app, socketio


@app.route("/")
def index():
    return "I'm alive!"

use_localhost = os.environ.get("IN_DOCKER", False) # and os.environ.get("REPL_ID", False)

if __name__ == "__main__":
    host = "127.0.0.1" if use_localhost else "0.0.0.0"
    socketio.run(
        app,
        debug=False,
        host=host,
        port=3000,
        #ssl_context=("cert.pem", "key.pem"),
    )
