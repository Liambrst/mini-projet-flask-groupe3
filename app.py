from flask import Flask, abort, render_template, request
import json

app = Flask(__name__)

def charger_donnees():
    with open("data/data.json", "r", encoding="utf-8") as fichier:
        return json.load(fichier)

@app.route("/")
def index():
    donnees = charger_donnees()

    return render_template(
        "index.html",
        donnees=donnees
    )

@app.route("/detail/<int:id>")
def detail(id):
    donnees = charger_donnees()

    element = next(
        (item for item in donnees if item["id"] == id),
        None
    )

    if element is None:
        abort(404)

    return render_template(
        "detail.html",
        element=element
    )

if __name__ == "__main__":
    app.run(debug=True)
