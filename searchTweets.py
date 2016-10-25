import json
import oauth2 as oauth
import os
import argparse

# parsing user input for the term to fetch tweets for
parser = argparse.ArgumentParser()
parser.add_argument("search",help = "enter the search term ") 
args = parser.parse_args()
query = args.search
#query = input("Enter Search Term : ")
query = query.lower()

# API call Arguments
CONSUMER_KEY = "kkDcIct3CMaPW8yYB88YLaVyL"
CONSUMER_SECRET = "6dWlU8yBR6t38lBneeW5FcxR1FCoJeIPipqNSCTHjfIxW8VtlK"
ACCESS_KEY = "456545130-uY5aKKUC9o2aoY9RxUGMtXdwQJnIjcNrXuFL6bR4"
ACCESS_SECRET = "PzVH3FBkMa9t9WWhhvHOzt9wPszdxcQbOObTr827CV3CO"
# Authenticating & constructing API call
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

# calling API to fetch tweets 
link = "https://api.twitter.com/1.1/search/tweets.json?q="+query+"&count=100"
resp , all_data = client.request(link)
# decoding to JSON format
tweets = json.loads(all_data.decode())
# storing non-duplicate tweets in a dictionary
data = {}
for tweet in tweets.get("statuses"):
	if tweet["lang"] == 'en':
		data[tweet["id"]] = tweet

file_name = query +".json"
json_files = [f_json for f_json in os.listdir(".") if f_json.startswith(query)]
if json_files:
    with open(json_files[0],'r') as data_file:  
        file_data = json.load(data_file)
    for ID in file_data:
        data[ID] = file_data[ID]
with open(file_name,'w') as f:
    json.dump(data,f)