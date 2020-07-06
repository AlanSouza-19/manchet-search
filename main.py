import urllib3
import json
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
r = http.request('GET', 'https://g1.globo.com/')
html_data = r.data.decode('utf-8')
html = BeautifulSoup(html_data, 'html.parser')

finder = html.find_all(class_='feed-post-link gui-color-primary gui-color-hover')

for i in finder:
  print(i.get_text())
