import json,os
from datetime import datetime
from dateutil import tz
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("startDate",help = "enter the Min Date in YYYY-MM-DD format") 
parser.add_argument("endDate",help = "enter the Max Date YYYY-MM-DD format") 

args = parser.parse_args()

date_start = args.startDate
date_end = args.endDate

date_start = datetime.strptime(date_start,'%Y-%M-%d')
date_end = datetime.strptime(date_end,'%Y-%M-%d')

best_tweet = {}

json_files = [f_json for f_json in os.listdir(".") if f_json.endswith(".json")]
for js in json_files:
    with open(js,'r') as data_file:  
        file_data = json.load(data_file)
    
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    popularity = {}
    retweet_count = 0
    for f in file_data:
        if file_data[f]["lang"] =="en":
            tweet_date = file_data[f]["created_at"]
            tweet_date = datetime.strptime(tweet_date,'%a %b %d %H:%M:%S +0000 %Y')
            tweet_date = tweet_date.replace(tzinfo=from_zone)
            tweet_date = tweet_date.astimezone(to_zone)
            tweet_date = datetime.strptime(str(tweet_date),'%Y-%m-%d %H:%M:%S-04:00')
            if(tweet_date <= date_end or tweet_date >= date_start):
                tweet = file_data[f]["text"].lower()
                retweet_count = file_data[f]["retweet_count"]
                if tweet not in popularity:
                    popularity[tweet] = retweet_count
                else:
                    popularity[tweet] = popularity[tweet] + retweet_count

    count = 0                   
    for w in sorted(popularity, key=popularity.get, reverse=True):
        count = count + 1
        if count <= 1:
            best_tweet[js[:-5]] = w
        else:
            break

for t in best_tweet:
    print(t,"\t \t",best_tweet[t])