# Scraping with Python

Presentation created for [Jugend hackt Zürich 2023](https://jugendhackt.org/events/schweiz/)

## Vorbereitung

- PGW: <https://www.pwg.ch/>
- Barnaby Skinner: <https://www.tagesanzeiger.ch/die-gutheissungsquoten-sinken-bei-allen-richtern-404322581374>
- DuckDuckGo: <https://duckduckgo.com> (F12 > Network)
- Progrssive loading: <https://www.nzz.ch/schweiz>
- Gitlab API: <https://gitlab.com/api/v4/projects/a.l.e%2Fadvent-of-code/repository/commits>
- OpenData: <https://data.stadt-zuerich.ch/>

## Notes

using pandoc to export to pdf

```sh
$ pandoc -t beamer scraping-with-python.md -o scraping-with-python.pdf
```

getting free images:

https://openverse.org

35C3 - Freude ist nur ein Mangel an Information 
https://www.youtube.com/watch?v=MRqWaRMFsPs


## Notes

When we search for "scraping" on DuckDuckGo, the "More Results" button gives us the following url in the Network tab of the Web Developer Tool:

`https://links.duckduckgo.com/d.js?q=scraping&a=h_&t=D&l=us-en&p=&s=28&ex=-1&dl=en&ct=CH&sp=0&vqd=x-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&biaexp=b&cast_exp=a&litexp=a&msvrtexp=b&typeexp=b&bpa=1&wrap=1`

Which we can reduce a little bit and where we can _extract `VQD`, which seems to be an ID unique to the request:

```
VQD = '4-60749118923287605789131552604296645186'
url = f'https://links.duckduckgo.com/d.js?q=scraping&a=h_&t=D&l=us-en&p=&s=08&ex=-1&dl=en&ct=CH&sp=0&vqd={VQD}'
```
