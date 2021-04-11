import requests
from bs4 import BeautifulSoup

# https://weworkremotely.com/remote-jobs/search?term=python

def extract_job_info(job_data):
    title = job_data.find("span", {"class": "title"}).text
    company = job_data.find("span", {"class": "company"}).text
    link = job_data.find_all("a")[1]["href"]
    return {"site": "weworkremotely", "title": title, "company": company, "link": f"https://weworkremotely.com{link}"}


def get_jobs(word):
    jobs = []
    #한 페이지에 모두 나옴
    print("get_jobs in wwr.py")
    request = requests.get(f"https://weworkremotely.com/remote-jobs/search?term={word}")
    soup = BeautifulSoup(request.text, "html.parser").find("section", {"class": "jobs"})
    if soup:
        jobs_data = soup.find_all("li")[:-1]
        for job_data in jobs_data:
            job = extract_job_info(job_data)
            jobs.append(job)
        return jobs
    else:
        return