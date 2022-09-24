#create a program that scrapes tweets using python

#import the required libraries

import pandas as pd
import snscrape.modules.twitter as sntwitter
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

#set up your query
#The data i intend to scrape and export to a dataframe are data based on tweets related to BBNaija

query = '(BBNaija) until:2022-09-30 since:2022-08-10'

#create an empty dataframe that would save the extracted tweets to a readable dataframe

tweets = []

limit = 1000 #scraping 100 tweets, you can set your desired limit

for tweet in sntwitter.TwitterHashtagScraper(query).get_items():
    if len (tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.url, tweet.user.username, tweet.sourceLabel, tweet.user.location, tweet.content, tweet.likeCount, tweet.retweetCount, tweet.quoteCount, tweet.replyCount])



#create the columns for your extracted tweet dataframe
scraped = pd.DataFrame(tweets,columns = ['Date','TweetsURL','Users','Source','Location','Tweets','Likes Count','Retweet Count','Tweet Quote_Count','Tweet Reply_Count'])


#perfrorm some basic EDA on the extracted tweet dataframe

print(scraped.head())
print(scraped.info())

#save the extracted tweet to a csv or excel file

scraped.to_csv('BBNaija7_Tweet.csv',sep= ',',index = False)

