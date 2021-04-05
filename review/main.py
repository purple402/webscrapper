from flask import Flask, render_template
from flask import Flask, render_template, request, redirect
from indeed import get_jobs as get_indeed_jobs

app = Flask("WebScrapper Review")

db = {}

@app.route('/')
def home():
    return render_template("index_review.html")

@app.route('/report')
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existing_job = db.get(word)
        if existing_job:
            jobs = existing_job
        else:
            jobs = get_indeed_jobs(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template("report_review.html", searching_by=word, jobs=jobs, results_number=len(jobs))

    


app.run(host="127.0.0.1", debug=True)