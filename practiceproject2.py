## SI 206 W17 - Project 2 

## COMMENT HERE WITH:
## Your name:
## Anyone you worked with on this project:

## Below we have provided import statements, comments to separate out the parts of the project, instructions/hints/examples, and at the end, tests. See the PDF of instructions for more detail. 
## You can check out the SAMPLE206project2_caching.json for an example of what your cache file might look like.

###########

## Import statements
import unittest
import json
import requests
import tweepy
import re
import twitter_info # Requires you to have a twitter_info file in this directory
from bs4 import BeautifulSoup

## Tweepy authentication setup
## Fill these in in the twitter_info.py file
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up to be able grab stuff from twitter with your authentication using Tweepy methods, and return it in a JSON format 
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

## Part 0 -- CACHING SETUP

## Write the code to begin your caching pattern setup here.

CACHE_FNAME = "206project2_caching.json"
try:
	cache_file = open(CACHE_FNAME,'r')
	cache_contents = cache_file.read()
	#CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}


## PART 1 - Define a function find_urls.
## INPUT: any string
## RETURN VALUE: a list of strings that represents all of the URLs in the input string

## For example: 
## find_urls("http://www.google.com is a great site") should return ["http://www.google.com"]
## find_urls("I love looking at websites like http://etsy.com and http://instagram.com and stuff") should return ["http://etsy.com","http://instagram.com"]
## find_urls("the internet is awesome #worldwideweb") should return [], empty list

def find_urls(string): 
	numlist = []
	matches = re.findall('^https?:\/\/(www.)?\w{2,}(?:\.+\w{2,})+', string) #remember second input of regex needs to match function input
	return matches 


## PART 2 (a) - Define a function called get_umsi_data.
## INPUT: N/A. No input.
## The function should check if there is any cached data for the UMSI directory in your cached file -- if so, return it, and if not, the function should access each page of the directory, get the HTML associated with it, append that HTML string to a list. The function should cache (save) that list when it is accumulated.
## RETURN VALUE: A list of HTML strings representing each page of the UMSI directory. 
## Reminder: you'll need to use the special header for a request to the UMSI site, like so:
#### requests.get(base_url, headers={'User-Agent': 'SI_CLASS'}) 

## Start with this page: https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All  
## End with this page: https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page=11 


def get_umsi_data(): 
	try:
		cache_file = open(CACHE_FNAME,'r')
		cache_contents = cache_file.read()
		return cache_contents
	except: 
		all_pages_list = ['https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All', 
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=1', 
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=2',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=3',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=4',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=5',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=6',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=7',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=8',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=9',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=10',
		'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All&page=11']

		all_page_html = []

		for page in all_pages_list: 
			r = requests.get(page, headers={'User-Agent': 'SI_CLASS'})
			umsi_text = r.text #receiving text attribute
			all_page_html.append(umsi_text)

		f = open(CACHE_FNAME, 'w') #opening the file to write to 
		f.write(all_page_html) #write the text object to the opened file
		f.close()

		return all_page_html


## PART 2 (b) - Create a dictionary saved in a variable umsi_titles 
## whose keys are UMSI people's names, and whose associated values are those people's titles, e.g. "PhD student" or "Associate Professor of Information"...

	umsi_titles = {}
	soup = BeautifulSoup(all_page_html,"html.parser")
	people = soup.find_all("div",{"class":"views-row"})
	for names in people: 
		div = soup.find_all("div",{'class':"field-items-even"})
		for hats in div: 
			item = turtles.find("div",{"property":"dc:title"})
			item2 = item.find_next_sibling("div")
			umsi_titles[hats] = {item:item2}
	print(umsi_titles)



## PART 3 (a) - Define a function get_five_tweets
## INPUT: Any string
## Behavior: See instructions. Should search for the input string on twitter and get results. Should check for cached data, use it if possible, and if not, cache the data retrieved.
## RETURN VALUE: A list of strings: A list of just the text of 5 different tweets that result from the search.




## PART 3 (b) - Write one line of code to invoke the get_five_tweets function with the phrase "University of Michigan" and save the result in a variable five_tweets.




## PART 3 (c) - Iterate over the five_tweets list, invoke the find_urls function that you defined in Part 1 on each element of the list, and accumulate a new list of each of the total URLs in all five of those tweets in a variable called tweet_urls_found. 





########### TESTS; DO NOT CHANGE ANY CODE BELOW THIS LINE! ###########

get_umsi_data()
