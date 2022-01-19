import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.alx.pl/pl/kontakt/")
soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find_all("p", {"class", "tel"})

for i in soup:
    soup = i.find("strong")
    print(soup.get_text())
