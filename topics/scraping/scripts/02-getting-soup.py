import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://www.tagesanzeiger.ch/' + \
    'die-gutheissungsquoten-sinken-bei-allen-richtern-404322581374')
# print(r.text)
soup = BeautifulSoup(r.text)
print(soup.find('figcaption').find('span'))

print(soup.find('figcaption').find('span', \
    class_=re.compile('^HtmlText_root.*')))

print(soup.find('figcaption').find('span', \
    class_=lambda e: \
        e.startswith('HtmlText_root') \
        if e else False))
