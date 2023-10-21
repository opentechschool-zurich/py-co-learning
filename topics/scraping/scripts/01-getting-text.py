import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.tagesanzeiger.ch/die-gutheissungsquoten-sinken-bei-allen-richtern-404322581374')
# print(r.text)
soup = BeautifulSoup(r.text, features='html.parser')
print(soup.get_text())
