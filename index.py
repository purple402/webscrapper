import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')
pages = []
for link in links:
    pages.append(link.find("span"))
print(pages[0:-1])