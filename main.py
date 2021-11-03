from bs4 import BeautifulSoup

import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
skills = job.find('span', class_='srp-skills').text.replace(' ','')
print(f'company name {company_name}')
print(f'skills {skills}')




