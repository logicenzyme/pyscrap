from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome("/opt/google/chrome/chromedriver")

book_list=[] #List to store name of the product
author_list=[] #List to store price of the product
rating_list=[] #List to store rating of the product
driver.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_unv_b_1_1318168031_1/258-1908111-4117239")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('span',{'class':'a-list-item'}):
    name=a.find('div', attrs={'class':'p13n-sc-truncated'})
    author=a.find('div', attrs={'class':'a-row a-size-small'})
    rating=a.find('div', attrs={'class':'a-icon-row a-spacing-none'})
    book_list.append(name.text)
    author_list.append(author.text)
    rating_list.append(rating.text)

df = pd.DataFrame({'Book Name':book_list,'Author':author_list,'Rating':rating_list})
df.to_csv('best_seller_books.csv', index=False, encoding='utf-8')
