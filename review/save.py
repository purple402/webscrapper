import csv

def save_to_file(word, jobs):
    file = open(f"{word}.csv", 'w', encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["site", "title", "company", "link"])
    for job in jobs:
         writer.writerow(list(job.values()))
    return 
