import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="UTF-8", newline='')
    # 윈도우즈의 경우 csv 모듈에서 데이타를 쓸 때 각 라인 뒤에 빈 라인이 추가되는 문제가 있는데, 이를 없애기 위해 (파이썬 3 에서) 파일을 open 할 때 newline='' 와 같은 옵션을 지정한다
    # http://pythonstudy.xyz/python/article/207-CSV-%ED%8C%8C%EC%9D%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
         writer.writerow(list(job.values()))
    return 

