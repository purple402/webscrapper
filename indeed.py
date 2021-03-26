import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        # int로 만들어주기 위해서는 숫자만 있어야하기 때문에
        # 처음부터 마지막 item을 자르고 for loop를 실행한다
        pages.append(int(link.string))
        # <a>안에 <span> 하나만 있고, 그 안에 string이 유일하기 때문에
        # link.find('span').string과 결과가 같다.
        
    max_page = pages[-1]
    return max_page
