from bs4 import BeautifulSoup
import time
import requests

print('Put some skills that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill} ')

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='

def find_job():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        time_posted = job.find('span', class_='sim-posted').span.text
        if 'few' in time_posted:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.print(f'company name: {company_name.strip()} \n')
                    f.print(f'skills: {skills.strip()} \n')
                    f.print(f'More info {more_info} \n')


if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60 )

