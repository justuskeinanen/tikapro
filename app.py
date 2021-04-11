from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jiikeina"
db = SQLAlchemy(app)

@app.route("/")
def index():
    
    friends = ["Riikka", "Justus", "Kirsi", "Sami", "J-P"]
    return render_template("index.html", message = "Friends List: ", items= friends)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name= request.form["name"])