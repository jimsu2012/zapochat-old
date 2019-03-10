import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

import json

from html_sanitizer import Sanitizer

sanitizer = Sanitizer()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

messages = {};

@app.route("/")
def index():
    return render_template("index.html", messages=json.dumps(messages).replace(u'<', u'\\u003c').replace(u'>', u'\\u003e').replace(u'&', u'\\u0026').replace(u"'", u'\\u0027'))

@app.route("/about")
def about():
    return render_template("about.html")

@socketio.on("join room")
def join(data):
    displayname = data["displayname"]
    roomname = data["roomname"]
    if roomname not in messages:
        messages[roomname] = []
        emit("create room", {"roomname": roomname}, broadcast=True)
        print("room created: " + roomname)
    join_room(roomname)
    emit("announce join", {"displayname": data["displayname"]}, room=data["roomname"])
    emit("update messages", {"messages": messages}, broadcast=True)

@socketio.on("send message")
def send(data):
    message = sanitizer.sanitize(data["message"])
    if message == '' or message == ' ':
        return
    if len(messages[data["roomname"]]) >= 100:
        messages[data["roomname"]].pop(0)
    messages[data["roomname"]].append({"displayname": data["displayname"], "message": sanitizer.sanitize(data["message"]), "timestamp": data["timestamp"]})
    emit("announce message", {"displayname": data["displayname"], "message": sanitizer.sanitize(data["message"]), "timestamp": data["timestamp"]}, room=data["roomname"])
    emit("update messages", {"messages": messages}, broadcast=True)

@socketio.on("send image")
def send_image(data):
    image_html = "<br><img src=\"" + data["url"] + "\"></img>"
    emit("announce message", {"displayname": data["displayname"], "message": image_html, "timestamp": data["timestamp"]}, room=data["roomname"])

if __name__ == "__main__":
    socketio.run(app)
