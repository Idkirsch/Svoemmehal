import requests
import json
import argparse
import os
from random_word import RandomWords
import tweepy
import asyncio
import time



# Initiate the parser
parser = argparse.ArgumentParser()

# parser.add_argument("-D", "--duplicates", help="nuke duplicates", action="store_true")
parser.add_argument("-w", "--word", help="word to search for")

# Read arguments from the command line
args = parser.parse_args()

app_id = "3a21b210"
app_key = '1159bf82a82b9bf8144789b889f568c4'
language = "en-gb"

# word_id = args.word
# word_id = RandomWords().get_random_word().replace('(', '').replace(')', '')

dump = None

# x = 1

def checkOxfordForRandomWord(dump):
 # word_id = RandomWords().get_random_word(hasDictionaryDef="true", 
 #    	includePartOfSpeech="noun", minCorpusCount=1, maxCorpusCount=10, 
 #    	minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
    word_id = RandomWords().get_random_word()
    print(word_id)
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    # print("dump: "+str(dump))
    if r.status_code == 200:
        dump = r.json()
        r = str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
        print("r: ", str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]))
        # x = 0
        return dump

try:

	word_id = RandomWords().get_random_word()
	print(word_id)
	url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
	r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
	# print("dump: "+str(dump))
	
	dump = r.json()
	r = str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
	print("r: ", str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]))
	# x = 0


	# dump = r.json()
	output = "A human being is like a "+word_id+": "+str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
	print("A human being is like a "+word_id+": "+str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]))
	os.system("say \""+output+"\"")

	# Authenticate to Twitter
	auth = tweepy.OAuthHandler("V17rp0sFfvBfVnFk4w7UIHZ2v", "EjjK5tpp5VvlKx7GROytYcU4ELAkCFSF7s0XEdP61tqOx8aG0G")
	auth.set_access_token("1035197003012161538-AopERnlGo3nUjVKXcfmc85VHX7rP6G", "W924j48mPpyOz1GMNMUexn2lFw1L13pu71ZekboOjv8u0")

	# Create API object
	api = tweepy.API(auth)

	# Create a tweet
	api.update_status(output)

	# while dump == None:
	# 	checkOxfordForRandomWord(dump)
	# 	time.sleep(10)
	# 	# print("dumpy: "+str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]))



	# if r != None:
	# 	# dump = r.json()
	# 	output = "A human being is like a "+word_id+": "+str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
	# 	print("A human being is like a "+word_id+": "+str(dump['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]))
	# 	os.system("say \""+output+"\"")

	# 	# Authenticate to Twitter
	# 	auth = tweepy.OAuthHandler("V17rp0sFfvBfVnFk4w7UIHZ2v", "EjjK5tpp5VvlKx7GROytYcU4ELAkCFSF7s0XEdP61tqOx8aG0G")
	# 	auth.set_access_token("1035197003012161538-AopERnlGo3nUjVKXcfmc85VHX7rP6G", "W924j48mPpyOz1GMNMUexn2lFw1L13pu71ZekboOjv8u0")

	# 	# Create API object
	# 	api = tweepy.API(auth)

	# 	# Create a tweet
	# 	api.update_status(output)
	# else:
	# 	print("I never got a response")


except Exception as e:
	print("Fejl: "+str(e))
	raise
else:
	pass
finally:
	pass









