import time
from secret import *
from getpass import getpass
from textwrap import TextWrapper

import tweepy


class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print self.status_wrapper.fill(status.text)
            print '\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source)

            print "Tweet Text: ",status.text

            text = status.text

            print "Time Stamp: ",status.created_at

            print "Time Stamp: ",status.created_at

            print "Source: ",status.source

            source = status.source

            print "Author: ",status.user.screen_name

            author = status.user.screen_name

            print "Name: ",status.user.name

            name = status.user.name

            print "Time Zone: ",status.user.time_zone

            time_zone = status.user.time_zone

            print "User Language: ",status.user.lang

            user_language = status.user.lang

            print "Followers: ",status.user.followers_count

            followers = status.user.followers_count

            print "User Description: ",status.user.description

            user_description = status.user.description

            print "Geo Enabled: ",status.user.geo_enabled

            geo_enabled = status.user.geo_enabled

            print "Friends: ",status.user.friends_count

            friends = status.user.friends_count

            print "Retweets: ",status.retweet_count

            retweets = status.retweet_count

            print "Location: ",status.user.location

            location = status.user.location

            print "ID: ",status.user.id_str

            user_id = status.user.id_str

            print "Coordinates: ",status.coordinates

            coordinates = status.coordinates

            print "Place: ",status.place

            place = status.place







        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing Zzzzzz'


def main():
    # Prompt for login credentials and setup stream object
#    consumer_key = raw_input('Consumer Key: ')
 #   consumer_secret = getpass('Consumer Secret: ')
 #   access_token = raw_input('Access Token: ')
 #   access_token_secret = getpass('Access Token Secret: ')




    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = tweepy.Stream(auth, StreamWatcherListener(), timeout=None)

    # Prompt for mode of streaming
    valid_modes = ['sample', 'filter']
    while True:
        mode = raw_input('Mode? [sample/filter] ')
        if mode in valid_modes:
            break
        print 'Invalid mode! Try again.'

    if mode == 'sample':
 #       stream.sample()
#        stream.filter(locations=[-33.095480,-71.809518,-34.108874,-69.859445])
        stream.filter(locations=[-71.288477,-33.960067,-70.090967,-33.050879])
    elif mode == 'filter':
        follow_list = raw_input('Users to follow (comma separated): ').strip()
        track_list = raw_input('Keywords to track (comma seperated): ').strip()
        if follow_list:
            follow_list = [u for u in follow_list.split(',')]
            userid_list = []
            username_list = []
            
            for user in follow_list:
                if user.isdigit():
                    userid_list.append(user)
                else:
                    username_list.append(user)
            
            for username in username_list:
                user = tweepy.API().get_user(username)
                userid_list.append(user.id)
            
            follow_list = userid_list
        else:
            follow_list = None
        if track_list:
            track_list = [k for k in track_list.split(',')]
        else:
            track_list = None
        print follow_list
        stream.filter(follow_list, track_list)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'