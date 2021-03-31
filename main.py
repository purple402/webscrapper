from flask import Flask, render_template, request

app = Flask("WebScrapper")

@app.route("/")
def home():
    return render_template("index.html")

app.run(host="127.0.0.1", debug=True)