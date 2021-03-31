from flask import Flask, render_template, request, redirect
from so import get_jobs 

app = Flask("WebScrapper")

db = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existing_jobs = db.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searching_by=word)

app.run(host="127.0.0.1", debug=True)