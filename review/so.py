import requests
from bs4 import BeautifulSoup

def get_last_page():
    request = requests.get("https://stackoverflow.com/jobs?q=python")
    soup = BeautifulSoup(request.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job_info(job_data):
    title = job_data.find("a", {"class": "s-link"})["title"]
    company_row = job_data.find("h3", {"class": "mb4"})
    company = company_row.find("span").get_text(strip=True)
    location = company_row.find("span", {"class": "fc-black-500"}).get_text(strip=True)
    job_id = job_data["data-jobid"]
    return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(1):
        job_page = requests.get(f"https://stackoverflow.com/jobs?q=python&pg={page}")
        soup = BeautifulSoup(job_page.text, "html.parser")
        jobs_in_page = soup.find_all("div", {"class": "-job"})
        for job_data in jobs_in_page:
            job = extract_job_info(job_data)
            jobs.append(job)
    return jobs


last_page = get_last_page()
jobs = extract_jobs(last_page)
