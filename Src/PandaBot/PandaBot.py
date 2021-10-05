import tweepy
import time
import yaml
import os.path

from yaml.loader import SafeLoader

class PandaBot:
    def __init__(self):
        # YAML Configuration path
        confPath = 'PandaBotConf.yaml'
        self.__lastModDate = 0

        # Read the configuration file
        with open(confPath) as f:
            confData = yaml.load(f, Loader=SafeLoader)

            self.__imagePath = confData['imagePath']
            self.__posPath = confData['positionPath']
            self.__sleepTime = confData['sleepTime']
            consumerKey = confData['consumerKey']
            consumerSecretKey = confData['consumerSecretKey']
            accessToken = confData['accessToken']
            accessTokenSecret = confData['accessTokenSecret']

        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(consumerKey, consumerSecretKey)
        auth.set_access_token(accessToken, accessTokenSecret)
        self.__api = tweepy.API(auth)

        # Check the authentication is correct 
        try:
            self.__api.verify_credentials()
            print("PandaBot initialilzed correctly :)")
        except:
            print("Error during authentication, bye :(")

    # Post an image tweet along with Panda position
    def post_on_twitter(self):
        latitude = 52.158832 # default values, i.e. Javi's Home
        longitude = 4.488657

        # Read the position in the file, TODO: close the file f?
        with open(self.__posPath) as f:
            posData = yaml.load(f, Loader=SafeLoader)
            latitude = posData['latitude']
            longitude = posData['longitude']

        tweetText = "Pandita is here: %fN, %fE" % (latitude, longitude)
        status =  self.__api.update_status_with_media(tweetText, self.__imagePath, lat = latitude, long = longitude, display_coordinates = True)
        print("New photo posted on twitter") # TODO: deal with status error

    # Run cyclically
    def run(self):
        # Enter the endless loop ...
        while (True):
            # Sleep for a while
            time.sleep(self.__sleepTime)

            # Get the last modified date for the image
            currentModDate = 0
            currentModDate = os.path.getmtime(self.__imagePath)

            # If we have a new image in the FS, then post it on tweeter
            if (currentModDate > self.__lastModDate):
                self.post_on_twitter()
                self.__lastModDate = currentModDate


# Run Panda Ruuuunnnn!!!!
desertPanda = PandaBot()
desertPanda.run()
