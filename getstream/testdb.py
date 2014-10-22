from secret import *
import MySQLdb
import time

db = MySQLdb.connect(host,user,passwd, db)
cursor=db.cursor()
add_test=("INSERT INTO TEST (ID) VALUES (%s)")
data=("1")

add_user=("INSERT INTO `USERS` (`ID_USER`,`NAME`,`TIMEZONE`,`LANGUAGE`,`FOLLOWERS`,`DESCRIPTION`) VALUES (%s,%s,%s,%s,%s,%s)")
data_user=('1','Juan','CL','ES',100,'hola soy juam y esta es mi descripcion')

add_tweet=("INSERT INTO `TWEETS` (`TEXT`,`CREATED_AT`,`RETWEETS`,`ID_USER`,`LOCATION`,`SOURCE`,`COORDINATES`,`PLACE`,`GEOENABLE`,`ID_TWITTER`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
data_tweet=('HOLA ESTE ES UN TWEET',time.time(),10,'1','3e12321,312321','android','stgo','aqui',1,'31231232131')

add_incident=("INSERT INTO `INCIDENTS` (`ID_TWEET`,`ID_ITYPE`) VALUES (%s,%s)")
data_incident=(1,2)

#def test():
try:
    cursor.execute(add_user,data_user)
except:
    pass

try:
   cursor.execute(add_tweet,data_tweet)
except:
    pass

cursor.execute(add_incident,data_incident)



cursor.execute("select * from USERS")

for reg in cursor:
    print(reg)

cursor.execute("select * from TWEETS")

for reg in cursor:
    print(reg)

cursor.execute("select * from INCIDENTS")

for reg in cursor:
    print(reg)



db.commit()
cursor.close()
db.close()
