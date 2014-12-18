import time
from secret import *
from getpass import getpass
from textwrap import TextWrapper
import tweepy
import MySQLdb


def ifTaco(text):
    palabrasTaco=['trafico','congestion','transito','semaforo','#trafico','#congestion','#transito','#semaforo','en','taco','#taco']
    i=0
    tweet=text.lower().split(' ')
    for palabra in palabrasTaco:
        if palabra in tweet:
            i=i+1
    return i

def ifAccidente(text):
    palabras=['accidente','accidentes','panne','choque','volcamiento','colision','#accidente','#accidentes','#panne','#choque','#volcamiento','#colision','en']
    i=0
    tweet=text.lower().split(' ')
    for palabra in palabras:
        if palabra in tweet:
            i=i+1
    return i

def addToDb(status):
    add_user=("INSERT INTO `USERS` (`ID_USER`,`NAME`,`TIMEZONE`,`LANGUAGE`,`FOLLOWERS`,`DESCRIPTION`) VALUES (%s,%s,%s,%s,%s,%s)")
    data_user=(status.user.id_str,status.user.name,status.user.time_zone,status.user.lang,status.user.followers_count,status.user.description)

    add_tweet=("INSERT INTO `tweets` (`text`,`created_at`,`retweets`,`id_user`,`location`,`sorce`,`coordinates`,`geoenable`,`id_twitter`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data_tweet=(status.text.econde('utf8'),status.created_at,status.retweet_count,status.user.id_str,status.user.location,status.source,status.coordinates.encode('utf8'),status.user.geo_enabled,status.id_str)

    add_incident=("INSERT INTO `INCIDENTS` (`ID_TWEET`,`ID_ITYPE`) VALUES (%s,%s)")
    data_incident=(1,2)
    cursor.execute(add_user,data_user)
    cursor.execute(add_tweet,data_tweet)
    db.commit()
    cursor.close()
    db.close()


class StreamWatcherListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')
    def on_status(self, status):
        try:
            db2 = MySQLdb.connect(host,user,passwd, db)
            cursor=db2.cursor()
            db2.set_character_set('utf8')
            cursor.execute('SET NAMES utf8;') 
            cursor.execute('SET CHARACTER SET utf8;')
            cursor.execute('SET character_set_connection=utf8;')
#            print(status.coordinates)           
#            print(status.coordinates[u'coordinates'])
            if status.coordinates:
                coor=status.coordinates[u'coordinates']
                lat=coor[1]
                lon=coor[0]
               # print coor[0],coor[1]
            else:
                coor=""
                lat=0
                lon=0

            add_user=("INSERT INTO `USERS` (`ID_USER`,`NAME`,`TIMEZONE`,`LANGUAGE`,`FOLLOWERS`,`DESCRIPTION`) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE FOLLOWERS="+str(status.user.followers_count))
            data_user=(status.user.id_str,status.user.name,status.user.time_zone,status.user.lang,status.user.followers_count,status.user.description)
            add_tweet=("INSERT INTO `tweets` (`text`,`created_at`,`retweets`,`id_user`,`source`,`coordinates`,`geoenable`,`id_twitter`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
 
            data_tweet=(status.text.encode('utf8'),status.created_at,status.retweet_count,status.user.id_str,status.source,str(lat)+"|"+str(lon),status.user.geo_enabled,status.id_str)
#            print(add_tweet,data_tweet)
            add_incident=("INSERT INTO `incidents` (`tweet_id`,`itype_id`,`latitude`,`longitude`,created_at,text,timestamp) VALUES (%s,%s,%s,%s,DATE_ADD(NOW(),INTERVAL -3 HOUR),%s,DATE_ADD(NOW(),INTERVAL -3 HOUR))")
            if(ifTaco(status.text)>=2 and lat!=0):
                data_incident=(status.id_str,1,lat,lon,status.text.encode('utf8'))
                cursor.execute(add_incident,data_incident)
                print '--SE HA DETECTADO TACO!!\n--'+status.text
            if(ifAccidente(status.text)>=2 and lat!=0):
                data_incident=(status.id_str,2,lat,lon,status.text.encode('utf8'))
                cursor.execute(add_incident,data_incident)
                print '--SE HA DETECTADO ACCIDENTE!!\n--'+status.text


 #cursor.execute(add_user,data_user)
            cursor.execute(add_tweet,data_tweet)
            db2.commit()
            cursor.close()
            db2.close()


        except Exception as e:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            print(e)
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
    i=0
    # Prompt for mode of streaming
    valid_modes = ['sample', 'filter']
    while True:

 #       stream.sample()
#        stream.filter(locations=[-33.095480,-71.809518,-34.108874,-69.859445])
         stream.filter(locations=[-71.288477,-33.960067,-70.090967,-33.050879])
         print i
         i=i+1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'
