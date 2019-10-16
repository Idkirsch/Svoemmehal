# We want to scrape data from the website of the local swimmingpool and later make an animation
#
# import pandas as pd
import requests
# from bs4 import BeautifulSoup
import time
# from selenium import webdriver
import json

yWas = None

i = 0
while i == 0:
	data = requests.get("https://l.vemcount.com/embed/data/W5mOsIMsECIwoYZ").content

# Find parser der kan læse json for at skaffe data
	y = json.loads(data)

	print(y['value'])

	# y = str(y)

	# print("antal svømmere: "+str(y['value']))
	# time.sleep(1)

	# afile = open('test.json','w')
	# afile.write(json.dumps(alerts,encoding='UTF-8'))
	# afile.close()

	# y = y.decode('utf-8')
	# print('yWas')
	# print(yWas)
	# print('y')
	# print(y)

	# if y == yWas:
		# print('its truuue')

	if yWas != y:
		with open('data.txt','w') as outfile:
			json.dump(y, outfile)
			# print('Am I ever done?')
			yWas = y
			print('What: '+ str(yWas))




