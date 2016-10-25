import json,os
from datetime import datetime
from dateutil import tz
from datetime import time
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import argparse

# parsing user input for the term to fetch tweets for
parser = argparse.ArgumentParser()
parser.add_argument("term",help = "enter the search term ") 
parser.add_argument("startDate",help = "enter the Min Date in YYYY-MM-DD format") 
parser.add_argument("endDate",help = "enter the Max Date YYYY-MM-DD format") 
parser.add_argument("count",help = "enter the length of the word list",type=int) 
args = parser.parse_args()

query = args.term
query = query.lower()

date_start = args.startDate
date_end = args.endDate

#query = "apple"
#date_start = "2016-10-24"
#date_end = "2016-10-26"
date_start = datetime.strptime(date_start,'%Y-%M-%d')
date_end = datetime.strptime(date_end,'%Y-%M-%d')

json_files = [f_json for f_json in os.listdir(".") if f_json.startswith(query)]
if json_files:
    with open(json_files[0],'r') as data_file:  
        file_data = json.load(data_file)
        

from_zone = tz.tzutc()
to_zone = tz.tzlocal()

tknzr = TweetTokenizer()

word_list={}
stop = stopwords.words('english')

for f in file_data:
    if file_data[f]["lang"] =="en":
        tweet_date = file_data[f]["created_at"]
        tweet_date = datetime.strptime(tweet_date,'%a %b %d %H:%M:%S +0000 %Y')
        tweet_date = tweet_date.replace(tzinfo=from_zone)
        tweet_date = tweet_date.astimezone(to_zone)
        tweet_date = datetime.strptime(str(tweet_date),'%Y-%m-%d %H:%M:%S-04:00')
        if(tweet_date <= date_end or tweet_date >= date_start):
            tokens=[]
            tokens = tknzr.tokenize(file_data[f]["text"].lower())
            for token in tokens:
                if token not in stop and len(token)>2 and token.endswith(query)==False and token.startswith(query)==False:
                    if token not in word_list :
                        word_list[token] = 1  
                    else:
                        word_list[token] = word_list[token]+1
max_count = args.count  
count = 0                     
for w in sorted(word_list, key=word_list.get, reverse=True):
	count = count + 1
	if count <= max_count:
		print(w,"\t \t \t", word_list[w])
	else:
		break