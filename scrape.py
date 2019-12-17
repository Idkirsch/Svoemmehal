# We want to scrape data from the website of the local swimmingpool and later make an animation

import requests
import time
import json
import psutil
# import matplotlib.pyplot as pyplot

# %matplotlib notebook
# plt.rcParams['animation.html'] = 'jshtml'

# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.show()


yWas = None

i = 0
while i == 0:
	data = requests.get("https://l.vemcount.com/embed/data/W5mOsIMsECIwoYZ").content
	y = json.loads(data)
	# print(y['value'])
	if yWas != y:
		with open('data.txt','w') as outfile:
			json.dump(y, outfile)
			# print('Am I ever done?')
			yWas = y
			print('What: '+ str(yWas))




