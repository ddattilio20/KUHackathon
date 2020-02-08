from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Returns a list of urls that search eBay for an item
def make_urls(names):
    # eBay url that can be modified to search for a specific item on eBay
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw="
    # List of urls created
    urls = []

    for name in names:
        # Adds the name of item being searched to the end of the eBay url and appends it to the urls list
        # In order for it to work the spaces need to be replaced with a +
        urls.append(url + name.replace(" ", "+") + "&_sop=15")

    # Returns the list of completed urls
    return urls


# Scrapes and prints the url
def ebay_scrape(urls):
    for url in urls:
        # Downloads the eBay page for processing
        res = requests.get(url)
        # Raises an exception error if there's an error downloading the website
        res.raise_for_status()
        # Creates a BeautifulSoup object for HTML parsing
        soup = BeautifulSoup(res.text, 'html.parser')
        # Prints the url, listed item name, and the price of the item
        print(url + "\n")


# Runs the code
# 1. Make the eBay url list
# 2. Use the returned url list to search eBay and scrape and print information on each item
name_list = ["dell laptops"]
urlList = make_urls(name_list)



count = 0
driver = webdriver.Chrome("C:/Users/micha/Downloads/chromedriver_win32/chromedriver")

ids = []  # List to store id of the product
products=[]  # List to store name of the product
prices=[]  # List to store price of the product
driver.get(urlList[0])

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('div', attrs={'class':'s-item__info clearfix'}):
    count += 1
    print(a)
    name = a.find('h3', attrs={'class': 's-item__title s-item__title--has-tags'})
    if (name == None):
        name = a.find('h3', attrs={'class': 's-item__title'})
    print(name.text)

    price = a.find('span', attrs={'class': 's-item__price'})
    print(price.text)

    # link = a.find('a', href=True, attrs={'class': 's-item__link'})
    # print()

    ids.append(count)
    products.append(name.text)
    prices.append(price.text)

print(count)
df = pd.DataFrame({'IDs':ids, 'Product Name':products, 'Price':prices})
df.to_csv('ebayProducts.csv', index=False, encoding='utf-8')