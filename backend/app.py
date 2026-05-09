from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.config['SECRET_KEY'] = 'ipl_secret_key'

socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
