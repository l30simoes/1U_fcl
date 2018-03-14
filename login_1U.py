"""
    instabot example

    Workflow:
        Follow users who post medias with hashtag.
"""

import sys
import os, os.path
import time
import random
from tqdm import tqdm
import argparse

import requests
import http.client
import urllib.request
import re
import json
import datetime

import itertools

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
# parser.add_argument('filename', type=str, nargs='+', help='filename')
args = parser.parse_args()

bot = Bot()
# bot.login(username=args.u, password=args.p,
#           proxy=args.proxy)

# bot.login(username='1sturban',password='FirstU12#')
bot.login(username='1nsta_bot001',password='Insta12#')
# bot.login(username="1nsta", password="InstaPass12#")

# bot.log()

MAX_RETRIES = 100
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
session.mount('https://', adapter)
session.mount('http://', adapter)

invalid_escape = re.compile(r'\\[0-7]{1,3}')  # up to 3 digits for byte values up to FF



def check_if_folder_exists(path):
	if not os.path.exists(path):
		os.makedirs(path)
		print ("Folder created - " + path)

def replace_with_byte(match):
    return chr(int(match.group(0)[1:], 8))

def repair(brokenjson):
    return invalid_escape.sub(replace_with_byte, brokenjson)

def removeUni (bio):
	
	ls = len (bio)
	bioS = bio.replace(r'\n', r" ")
	bc = bioS

	uniArray = []

	# Get all Unicode from string and creating and array
	for x in range(0, ls):
		f = bc.find(r'\u')
		rep = bc[f:f+6]
		bc = bc.replace(rep, '')
		uniArray.append(rep)
		
	uniArray = [x for x in uniArray if x] # Remove empty items from array

	# Read array and replace bio
	for x in range(0, len(uniArray)):
		uniCode = uniArray[x] 
		# print (uniCode)

		f = bioS.find(uniCode)
		rep = bioS[f:f+6]
		bioS = bioS.replace(rep, r' ')

	return (bioS) 


def get_userid_from_username(username):
	sUrl = "http://www.instagram.com/%s/?__a=1" % (str(username.rstrip()))
	rUrl = session.get(sUrl) # Response URL
	username = username.rstrip()
	
	user_id = ''

	if rUrl.status_code == 429:

		ctime =  datetime.datetime.now()
		currentTime = str(ctime.hour) + ":" + str(ctime.minute) + ":" + str(ctime.second) + " - " + str(ctime.day) +"/"+ str(ctime.month) +"/"+ str(ctime.year)
		print ("\n" + str(count) + ") " + username)
		print ("Error 429 - Too many requests! // " + str(sleepTime) + " seconds standby...")
		print ("START: " + startTime + " // NOW  : " + currentTime) 
		print ("\n\n")

		time.sleep(sleepTime)

	if rUrl.status_code == 200:

		d = rUrl.content
		r = json.loads(d.decode('utf-8'))

		user_id = json.dumps(r['user']['id'])

	return user_id.replace('"','')



def cleantxt (filepath, filename): #remove duplicated lines
	
	path_file = filepath + filename
	uniqlines = set(open(path_file).readlines())
	htFile = open(path_file,'w').writelines(set(uniqlines))



