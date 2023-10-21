import requests

url = 'https://gitlab.com/api/v4/projects/' + \
    'a.l.e%2Fadvent-of-code/repository/commits'
response = requests.get(url)

if response.ok:
    print('yo')
    print(response.json()[0]['title'])
else:
    print(response.status_code)
