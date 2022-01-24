import requests
import json
import sys
import re
sys.path.append("/Users/apple/Code/Python/webcrap-hyp/__venv__/lib/python3.9/site-packages/bs4")
from bs4 import BeautifulSoup

url = 'https://www.hyperia.sk/kariera/'
r = requests.get(url)
link_list=[]
data = []

soup = BeautifulSoup(r.content, 'html.parser')
for a in soup.find_all('a', href=True, class_='arrow-link'):
    adress='http://www.hyperia.sk'+(a['href'])
    link_list.append(adress)

print(link_list)
for link in link_list:
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find_all('h1')[0].text.strip()
    place = soup.find_all('div', class_ = 'col-md-4 icon')[0].text.split(':')
    salary = soup.find_all('div', class_ = 'col-md-4 icon')[1].text.split('ohodnotenie')
    contract_type = soup.find_all('div', class_ = 'col-md-4 icon')[2].text.split(',')
    contact_email = soup.find_all('a', href=re.compile(r"^mailto:"))[0].get('href').split(':')

    print('title:',title.strip())
    print('place:',place[1].strip())
    print('salary:',salary[1].strip())
    print('contract_type:',contract_type[1].strip())
    print('contact_email:',contact_email[1].strip())
    scrap = {'title': title,'place': place[1],'salary': salary[1],'contract_type': contract_type[1],'contact_email': contact_email[1]}
    data.append(scrap)

with open("sample.json", "w", encoding='utf-8' ) as outfile:
    json.dump(data, outfile, ensure_ascii=False)

with open('hyp.txt','w',encoding='utf-8') as json_file:
    json.dump(data,json_file,ensure_ascii=False)
