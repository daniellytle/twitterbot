import sys, json, time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

query = sys.argv[1]
allTweets = []

consumer_key = "aWVOGpooY0fUdsM6kWmRPlzLn"
consumer_secret = "aoqWgsg4DNLfZhXb6DbOe1kXDyHbsSmkDQiy6idZnZnhmVwtJT"

access_token = "1718069682-gv4wz2OZYr68lfvF4TzKwsc9atMNy5WYZemKshy"
access_token_secret = "fxE3ZOIHjWCmCHegy9AaVM89f4YULZe8oniSZWjj8qfh7"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
    	tweet = json.loads(data)['text'].encode('ascii', 'ignore') + '\n'
    	print tweet
        # allTweets.append(tweet)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    tweets = stream.filter(languages=['en'], track=['trump', 'makeamericagreatagain', 'cruz', 'trump2016', 'kasich'])
    tweets.filter(locations=[-124.77,24.52,-66.95,49.38])

'''

So the above part sets up the stream and reads in tweets, filtered by language, keywords, and then by location (within the US).
The stuff below was my attempt to get it to return a limited number tweets. 
or like one tweet every few seconds but I couldn't figure it out. I think it has something to do with setting async=True in filter()
but like idk how exactly. If you can figure it out that would be dank

'''


'''
	while True:
		if stream.running is True:
			stream.disconnect()
			print allTweets.pop()
		else:
			print 'Streaming'
			stream.filter(languages=['en'], track=['trump', 'makeamericagreatagain', 'cruz', 'trump2016', 'kasich'], async=True)
			print 'here?'
			#tweets.filter(locations=[-124.77,24.52,-66.95,49.38], async=True)
		time.sleep(2)
'''
