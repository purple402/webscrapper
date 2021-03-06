import requests
from bs4 import BeautifulSoup

def get_last_page(word):
    request = requests.get(f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q={word}&limit=50")
    soup = BeautifulSoup(request.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("li")
    last_page = pages[-2].find("span").get_text()
    return int(last_page)


def extract_job_info(job_data):
    title = job_data.find("a", {"class": "jobtitle"}).get_text(strip=True)
    company_row = job_data.find("div", {"class": "sjcl"})
    if company_row.find("a"):
        company = company_row.find("a").get_text(strip=True)
    else:
        company = company_row.find("span").get_text(strip=True)
    location = company_row.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = job_data["data-jk"]
    return {"site": "indeed", "title": title, "company": company, "location": location, "link": f"https://kr.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page, word):
    jobs = []
    for page in range(last_page):
        print(f"scrapping inndeed page: {page}")
        request = requests.get(f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q={word}&limit=50&start={page}")
        soup = BeautifulSoup(request.text, "html.parser")
        jobs_in_page = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for job_data in jobs_in_page:
            job = extract_job_info(job_data)
            jobs.append(job)
    return jobs

def get_jobs(word):
    print(f"get_jobs in indeed.py")
    last_page = get_last_page(word)
    jobs = extract_jobs(last_page, word)
    return jobs