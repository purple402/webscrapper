from flask import Flask, render_template, request

app = Flask("WebScrapper")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    return "this is the report"

app.run(host="127.0.0.1", debug=True)