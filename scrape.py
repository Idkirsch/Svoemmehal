# We want to scrape data from the website of the local swimmingpool and later make an animation
#
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver


driver=webdriver.Chrome(executable_path=r"C:/Program Files (x86)/chromedriver")
driver.get("https://svoemkbh.kk.dk/hilleroedgade-bad")

noget = driver.find_element_by_name("description")
nogetAndet = noget.get_attribute("innerHTML")
print(nogetAndet)

# Wait 5 seconds before scraping 
# time.sleep(5)


# res = requests.get("https://svoemkbh.kk.dk/hilleroedgade-bad")
# print(res)



# soup = BeautifulSoup(res.content, features="html.parser")
# print(soup)


# table = soup.find_all('') 
# df = pd.read_html(str(table))
# print(df[0].to_json(orient='records'))