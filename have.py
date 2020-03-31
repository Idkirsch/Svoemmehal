from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from selenium.webdriver.common.by import By

import time
import os
import glob

from io import TextIOWrapper
import codecs

import sys
from datetime import datetime, timedelta
import re


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") # needed for download to specific directory ... 

# SKIFT PATH TIL DEN PATH DU LÆGGER CHROMEDRIVEREN PÅ:
driver = webdriver.Chrome(executable_path=r'/Users/kkr/chromedriver', options=chrome_options)

def super_get(url):
    driver.get(url)
    driver.execute_script("window.onbeforeunload = function() {};")



firstTime = True
x = 1

while firstTime: 
	super_get("http://utterslevdal.123hjemmeside.dk/277767321");
	assert "Venteliste" in driver.title


	fullSource = driver.execute_script("return document.documentElement.innerText")
	print(fullSource)
	firstTime = False
	time.sleep(3)
	# driver.close()
	# driver.quit()

while x:
	super_get("http://utterslevdal.123hjemmeside.dk/277767321");
	assert "Venteliste" in driver.title


	newSource = driver.execute_script("return document.documentElement.innerText")


	if newSource != fullSource:
		print(newSource)
		print('IT CHANGED')
		os.system("say \"It changed. Oh my God!\"")
		x = -1

	else:
		print('Still the same')
		# os.system("say \"It changed. Oh my God!\"")
		time.sleep(10)
