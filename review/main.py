from flask import Flask, render_template

app = Flask("WebScrapper Review")

@app.route('/')
def home():
    return render_template("index_review.html")

app.run(host="127.0.0.1", debug=True)