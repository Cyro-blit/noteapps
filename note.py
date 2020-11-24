from flask import Flask, render_template, request
from datetime import datetime
from json import load, dump #load - get data ,  dump- save data


note_app = Flask(__name__)

def load_note():
    with open('note.json','r') as file:
        return load(file)
def save_note(data):
    with open('note.json','w') as file:
        dump(data, file)
    return True
notes = load_note()

@note_app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        title = request.form.get("title")
        note = request.form.get("note")
        today = datetime.now()
        notes[title] = {
            "note" : note,
            "date" : "Posted :"+f"{today.day}-{today.month}-{today.year}-{today.hour}"
        }
        save_note(notes)

    return render_template("index.html", notes=notes)
