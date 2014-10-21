from secret import *
import MySQLdb

db = MySQLdb.connect(host,user,passwd, db)
cursor=db.cursor()
add_test=("INSERT INTO TEST (ID) VALUES (%s)")
data=("1")

add_tweet=("INSERT INTO `TWEETS` (`TEXT`,`CREATED_AT`,`RETWEETS`,`ID_USER`,`LOCATION`,`SOURCE`,`COORDINATES`,`PLACE`,`GEOENABLE`,`ID_TWITTER`,`new field`) VALUES ('','','%s','%s','%s','%s','%s','%s','%s','%s','%s')")
add_user=("INSERT INTO `USERS` (`ID_USER`,`NAME`,`TIMEZONE`,`LANGUAGE`,`FOLLOWERS`,`DESCRIPTION`) VALUES ('%s','%s','%s','%s','%s','%s')")

add_incident("INSERT INTO `INCIDENTS` (`ID_INCIDENT`,`ID_TWEET`,`ID_ITYPE`) VALUES ('','','')")



for x in range(0,100):

	cursor.execute(add_test,x)

cursor.execute("SELECT * FROM TEST")

for RID,ID in cursor:
    print(RID,ID)
db.commit()
cursor.close()
db.close()
