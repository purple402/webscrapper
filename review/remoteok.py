import requests
from bs4 import BeautifulSoup

# https://remoteok.io/remote-dev+python-jobs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_job_info(job_data):
    title = job_data.find("td", {"class": "position"}).find("h2").text
    company = job_data['data-company']
    link = job_data['data-url']
    return {"site": "remoteok", "title": title, "company": company, "link": f"http://remoteok.io{link}"}


def get_jobs(word):
    jobs = []
    #한 페이지에 모두 나옴
    print("get_jobs in remoteok.py")
    request = requests.get(f"https://remoteok.io/remote-dev+{word}-jobs", headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")
    jobs_table = soup.find("table")
    jobs_data = jobs_table.find_all("tr", {"class": "job"})
    for job_data in jobs_data:
        if 'closed' in job_data['class']:
            continue
        else:
            job = extract_job_info(job_data)
            jobs.append(job)
    return jobs
