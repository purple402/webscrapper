from flask import Flask, render_template, request, redirect

app = Flask("WebScrapper")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
    else:
        return redirect("/")
    return render_template("report.html", searching_by=word)

app.run(host="127.0.0.1", debug=True)