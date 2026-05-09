from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.config['SECRET_KEY'] = 'ipl_secret_key'

socketio = SocketIO(app, cors_allowed_origins="*")


# LOGIN PAGE
@app.route("/")
def login():
    return render_template("login.html")


# MAIN LOBBY PAGE
@app.route("/home")
def home():
    return render_template("index.html")


# ROOM PAGE
@app.route("/room")
def room():
    return render_template("room.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
