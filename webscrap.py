import requests
import json
import sys
import re
sys.path.append("/Users/apple/Code/Python/webcrap-hyp/__venv__/lib/python3.9/site-packages/bs4")
from bs4 import BeautifulSoup

url = 'https://www.hyperia.sk/kariera/'
r = requests.get(url)
link_list=[]

soup = BeautifulSoup(r.content, 'html.parser')
for a in soup.find_all('a', href=True, class_='arrow-link'):
    adress='http://www.hyperia.sk'+(a['href'])
    link_list.append(adress)

print(link_list)
for link in link_list:
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find_all('h1')
    contact_email = soup.find_all('a', href=re.compile(r"^mailto:"))
    print(title)
    print(contact_email)
    