import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
url = "https://allo.ua/"
url = "https://allo.ua/ua/smart-chasy/"
header = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
responce = session.get(url, headers=header)
print(responce)
soup = BeautifulSoup(responce.text, "lxml")

products = soup.find("div", class_="products-layout__container products-layout--grid")
prod = products.find_all("div", class_="product-card")

for elem in prod:
    title = elem.find('a', class_="product-card__title").text
    price = elem.find('div', class_="v-pb__cur discount")
    if price is not None:
        price = price.text
    print(title, price)