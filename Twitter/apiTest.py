from twitter import *


token = "937022771862917125-nf2TWDbpvPMifaxW9CoscoSIjxPxzsz"
token_secret = 	"jPRcm4WRfjkfPgnxfC5bAE16AEUiPTltvfUao5VoQNvD2"
consumer_key = 	"EJCObrUdZdjHxaibMjN8EMT3S"
consumer_secret = "oKvIkUIYfSbzvBwASHpDZ4rxHnBMnddVOQzrgRnURE5Y0H0UyN"

t = Twitter(auth=OAuth(token, token_secret, consumer_key,consumer_secret), retry=True)



test = t.statuses.home_timeline()
print (test)

def twitSearch (param):
    results = []
    for x in range (100):
        results.append( t.search.tweets( q="%s" % (param) ))
    return results

searchTerm = input("Enter test search term:    ")
searchResults = twitSearch(searchTerm)

for x in range (10):
    print (searchResults[x]['user']['tweet'])
    print ("\n\n")
