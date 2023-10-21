import requests
from pathlib import Path

requests_cache = Path('./requests-cache.html')
if not requests_cache.is_file():
    r = requests.get('https://www.tagesanzeiger.ch/die-gutheissungsquoten-sinken-bei-allen-richtern-404322581374')
    with open(requests_cache, 'w') as cache_file:
        cache_file.write(r.text)
with open(requests_cache, 'r') as cache_file:
    html = cache_file.read()
print(html)
