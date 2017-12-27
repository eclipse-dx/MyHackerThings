# ---------- TWITTER API INTERACTION CODE --------------
# Written by Tumi Lengoasa during UHack 2017

from twitter import *
import json

token = "937022771862917125-nf2TWDbpvPMifaxW9CoscoSIjxPxzsz"
token_secret = 	"jPRcm4WRfjkfPgnxfC5bAE16AEUiPTltvfUao5VoQNvD2"
consumer_key = 	"EJCObrUdZdjHxaibMjN8EMT3S"
consumer_secret = "oKvIkUIYfSbzvBwASHpDZ4rxHnBMnddVOQzrgRnURE5Y0H0UyN"

t = Twitter(auth=OAuth(token, token_secret, consumer_key,consumer_secret), retry=True)

# test = t.statuses.home_timeline()
# print (test)

# test2 = []
# test2 = t.search.tweets(q="?l=en&q=#bitcoin")

# print (test2)

# def twitSearch (param):
#     results = []
#     for x in range (100):
#         results.append( t.search.tweets( q="%s" % (param) ))
#     return results

positive_file = open(positive_tweets.dat, w+)
negative_file = open(negative_tweets.dat, w+)

def twitSearch (param):
    results = t.search.tweets( q="%s" % (param) )
    return results

def text(searchDict):
    num_elem = len(searchDict['statuses'])

    output = []
    for x in range (num_elem):
        current_tweet = searchDict['statuses'][x]
        current_date = searchDict['statuses'][x]['created_at']
        current_text = searchDict['statuses'][x]['text']
        is_RT = searchDict['statuses'][x]['retweeted']

        if (is_RT == False):
            output.append( (searchDict['statuses'][x]['text']) )
        print (searchDict['statuses'][x]['created_at'] + "\t" + searchDict['statuses'][x]['text'] + "\n")
    return output

searchTerm = input("Enter test search term:    ")
searchResults = twitSearch(searchTerm)


# print (searchResults['statuses'][0]['text'])
print (text(searchResults))


# print (searchResults)

# for x in range (2):
#     # print (searchResults[x]['user']['screen_name'])
#     print (searchResults[x])
#     print ("\n\n")
