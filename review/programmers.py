import requests
from bs4 import BeautifulSoup


def get_last_page(word):
    url = f"https://programmers.co.kr/job?job_position%5Btags%5D%5B%5D={word}"
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    pagination = soup.find("nav", {"class": "pagination"})
    if pagination:
        pages = pagination.find_all("li", {"class": "page-item"})
        last_page = pages[-2].find("a").text
        return int(last_page)
    else:    
        return None

def extract_job_info(job_data):
    body = job_data.find("div", {"class": "item-body"})
    title = body.find("h5", {"class": "position-title"}).get_text(strip=True)
    company_row = body.find("h6", {"class": "company-name"})
    inner_span = company_row.find("span")
    if inner_span:
        inner_span.decompose()
    company = company_row.get_text(strip=True)
    location = body.find("li", {"class": "location"})
    if location:
        location = location.get_text(strip=True)
    else:
        location = "no location"
    job_id = body.find("h5", {"class": "position-title"}).find("a")['href']
    return {"site": "programmers", "title": title, "company": company, "location": location, "link": f"https://programmers.co.kr/{job_id}"}

def extract_jobs(last_page, word):
    jobs = []
    for page in range(last_page):
        print(f"scraping programmers page : {page}")
        request = requests.get(f"https://programmers.co.kr/job?job_position%5Btags%5D%5B%5D={word}&page={page+1}")
        soup = BeautifulSoup(request.text, "html.parser")
        jobs_in_page = soup.find_all("li", {"class": "list-position-item"})
        for job_data in jobs_in_page:
            job = extract_job_info(job_data)
            jobs.append(job)
    return jobs

def get_jobs(word):
    print(f"get_jobs in programmers.py")
    last_page = get_last_page(word)
    if last_page == None:
        return print(f"no {word} jobs in programmers.com")
    jobs = extract_jobs(last_page, word)
    return jobs