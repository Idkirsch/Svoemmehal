# We want to scrape data from the website of the local swimmingpool and later make an animation
#
# import pandas as pd
import requests
# from bs4 import BeautifulSoup
import time
# from selenium import webdriver
import json


i = 0
while i == 0:
	data = requests.get("https://l.vemcount.com/embed/data/W5mOsIMsECIwoYZ").content

# Find parser der kan læse json for at skaffe data
	y = json.loads(data)
	print("antal svømmere: "+str(y["value"]))
	time.sleep(1)