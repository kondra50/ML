import requests
from bs4 import BeautifulSoup

url='https://www.yellowpages.com/search?search_terms=coffe&geo_location_terms=walnutcreek'

r= requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

links= soup.find_all("a")

for link in links:
    if not str(link.get('href')).find("http"):
       print(link.get('href'))



divs=soup.find_all("div",{"class":"info"})




for div in divs:
    print(div.contents[0].find_all("a",{"class":"business-name"}))
    print(div.contents[1].text)
