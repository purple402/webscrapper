from flask import Flask, render_template, request, redirect, send_file
from datetime import date
from so import get_jobs as get_so_jobs
from remoteok import get_jobs as get_ro_jobs
from wwr import get_jobs as get_wwr_jobs
from save import save_to_file

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""


app = Flask("Remote Job Scrapper")

db = {}

def get_date():
    month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    today = date.today()
    mon = today.month
    day = today.day
    return {"month": month[mon-1], "day": day}
    

@app.route('/')
def home():
    return render_template("index_review.html")

@app.route('/report')
def report():
    date = get_date()
    jobs = []
    word = request.args.get("word")
    if word:
        word = word.lower()
        existing_job = db.get(word)
        if existing_job:
            jobs = existing_job
        else:
            wwr_jobs = get_wwr_jobs(word)
            ro_jobs = get_ro_jobs(word)
            so_jobs = get_so_jobs(word)
            if wwr_jobs:
                jobs += wwr_jobs
            if ro_jobs:
                jobs += ro_jobs
            jobs += so_jobs
            db[word] = jobs
    else:
        return redirect('/')
    return render_template("report_review.html", searching_by=word, jobs=jobs, results_number=len(jobs), date=date)


@app.route('/export')
def export():
    word = request.args.get("word")

    jobs = db.get(word)
    save_to_file(word, jobs)
    print("save file")
    return send_file(f"{word}.csv", mimetype="text/csv", as_attachment=True)



    
app.run(host="127.0.0.1", debug=True)