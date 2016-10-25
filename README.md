# Basic Analysis of Twitter Data using Python

This repository helps in doing very basic analysis on twitter data using Twitter Search API (not streaming).
Following are the files in this repository and example command to use them.Please run searchTweets.py before running any other file:

python searchTweets.py apple

python userReach.py 2016-10-23 2016-10-27
                 
python wordCount.py apple 2016-10-24 2016-10-26 30
                 
python topTimeZones.py apple 2016-10-24 2016-10-26 10
                 
python topTweets.py cricket 2016-10-24 2016-10-26 5

python bestTweet.py 2016-10-23 2016-10-27
    
####for Help on arguments: python scriptName.py -h



####searchTweets :
This script will fetch 100 tweets from Twitter for the given input and saves the data in JSON format.


####userReach :
For all the terms searched in searchTweets, this script will give the extent of reach of users this "term" has for given range of date.


####wordCount :
For a inputted term (for which data fetched in searchTweets), this script will give the buzz words related to the term for given range of date. Number of buzz words required can also be be passed as an input.


####topTimeZones :
For a inputted term (for which data fetched in searchTweets), this script will give the top Time zones from where the people tweet related to the term for given range of date. Number of top time zones required can also be be passed as an input.


####topTweets :
For a inputted term (for which data fetched in searchTweets), this script will give the top retweeted plus favorited tweet for given range of date. Number of top tweets required can also be be passed as an input.


####bestTweet :
For all the terms searched in searchTweets, this script will give the best tweet of each "term" for given range of date.

