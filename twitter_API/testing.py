import tweepy

from tweepy.utils import import_simplejson
from tweepy.models import Status



# AUTHENTICATION KEYS
consumer_key="QOHQVbSfOPYT4gQ3QAhKftnF1"
consumer_secret="XvGpEJ5ePmkx8XKkI2kKE02FWdTtODue4dfYf5uJdC7l54xp7h"
access_token="1645116174-Ttk5sijJTzXsu6kLfMzEzWoXe7BlJCJcCe5DYl3"
access_token_secret="IpcD8K5UthAZNoVSmBZ0VF9WKbTOWxjHiZaC3Ohu8j2WZ"


# Authenticate User
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Play with API
# **********************************************************************
#msg="hello from python again"
#api.update_status(msg)


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        """Called when raw data is received from connection.
            Override this method if you wish to manually handle
            the stream data. Return False to stop stream and close connection.
        """
        json = import_simplejson()
        data = json.loads(raw_data)

        if 'friends' in data:
            print("someone followed me")




myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['python'])