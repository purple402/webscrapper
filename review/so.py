import requests
from bs4 import BeautifulSoup

def get_last_page(word):
    request = requests.get(f"https://stackoverflow.com/jobs?r=true&q={word}")
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
    return {"site": "stack overflow", "title": title, "company": company, "link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page, word):
    jobs = []
    if last_page > 10:
        last_page = 10

    for page in range(last_page):
        print(f"scrapping so page: {page}")
        job_page = requests.get(f"https://stackoverflow.com/jobs?r=true&q={word}&pg={page}")
        soup = BeautifulSoup(job_page.text, "html.parser")
        jobs_in_page = soup.find_all("div", {"class": "-job"})
        for job_data in jobs_in_page:
            job = extract_job_info(job_data)
            jobs.append(job)
    return jobs

def get_jobs(word):
    print(f"get_jobs in so.py")
    last_page = get_last_page(word)
    jobs = extract_jobs(last_page, word)
    return jobs