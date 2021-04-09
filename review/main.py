from flask import Flask, render_template, request, redirect
from datetime import date
from so import get_jobs as get_so_jobs
from indeed import get_jobs as get_indeed_jobs
from programmers import get_jobs as get_pro_jobs

app = Flask("WebScrapper Review")

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
    word = request.args.get("word")
    if word:
        word = word.lower()
        existing_job = db.get(word)
        if existing_job:
            jobs = existing_job
        else:
            indeed_jobs = get_indeed_jobs(word)
            so_jobs = get_so_jobs(word)
            pro_jobs = get_pro_jobs(word)
            if pro_jobs:
              jobs = pro_jobs + indeed_jobs + so_jobs
            else:
              jobs = indeed_jobs + so_jobs
            db[word] = jobs
            
    else:
        return redirect('/')
    return render_template("report_review.html", searching_by=word, jobs=jobs, results_number=len(jobs), date=date)

    
app.run(host="127.0.0.1", debug=True)