When we search for "scraping" on DuckDuckGo, the "More Results" button gives us the following url in the Network tab of the Web Developer Tool:

`https://links.duckduckgo.com/d.js?q=scraping&a=h_&t=D&l=us-en&p=&s=28&ex=-1&dl=en&ct=CH&sp=0&vqd=x-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&biaexp=b&cast_exp=a&litexp=a&msvrtexp=b&typeexp=b&bpa=1&wrap=1`

Which we can reduce a little bit and where we can _extract `VQD`, which seems to be an ID unique to the request:

```
VQD = '4-60749118923287605789131552604296645186'
url = f'https://links.duckduckgo.com/d.js?q=scraping&a=h_&t=D&l=us-en&p=&s=08&ex=-1&dl=en&ct=CH&sp=0&vqd={VQD}'
