import json,os
from datetime import datetime
from dateutil import tz
import argparse

# parsing user input for the term to fetch tweets for
parser = argparse.ArgumentParser()
parser.add_argument("term",help = "enter the search term ") 
parser.add_argument("startDate",help = "enter the Min Date in YYYY-MM-DD format") 
parser.add_argument("endDate",help = "enter the Max Date YYYY-MM-DD format") 
parser.add_argument("count",help = "enter the no. of top tweets to see",type=int) 
args = parser.parse_args()

query = args.term
query = query.lower()

date_start = args.startDate
date_end = args.endDate

date_start = datetime.strptime(date_start,'%Y-%M-%d')
date_end = datetime.strptime(date_end,'%Y-%M-%d')
popularity = {}

json_files = [f_json for f_json in os.listdir(".") if f_json.startswith(query)]
if json_files:
    with open(json_files[0],'r') as data_file:  
        file_data = json.load(data_file)

from_zone = tz.tzutc()
to_zone = tz.tzlocal()
dates = []
reach = 0
for f in file_data:
    if file_data[f]["lang"] =="en":
        tweet_date = file_data[f]["created_at"]
        tweet_date = datetime.strptime(tweet_date,'%a %b %d %H:%M:%S +0000 %Y')
        tweet_date = tweet_date.replace(tzinfo=from_zone)
        tweet_date = tweet_date.astimezone(to_zone)
        tweet_date = datetime.strptime(str(tweet_date),'%Y-%m-%d %H:%M:%S-04:00')
        if(tweet_date <= date_end or tweet_date >= date_start):
            tweet = file_data[f]["text"].lower()
            reach = file_data[f]["retweet_count"] + file_data[f]["favorite_count"]
            popularity[tweet] = reach

max_count = args.count    
count = 0                   
for w in sorted(popularity, key=popularity.get, reverse=True):
    count = count + 1
    if count <= max_count:
        print(popularity[w],"\t ", w)
    else:
        break