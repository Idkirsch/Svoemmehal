# We want to scrape data from the website of the local swimmingpool and later make an animation
#
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://svoemkbh.kk.dk/hilleroedgade-bad")
soup = BeautifulSoup(res.content,'html')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))
