import time
from secret import *
from getpass import getpass
from textwrap import TextWrapper
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

try:
    db2 = MySQLdb.connect(host,user,passwd, db)
    cursor=db2.cursor()
except Exception as e:
    print e
cursor.execute("select text,coordinates,date_add(created_at,interval -3 hour) from tweets WHERE date_add(created_at,interval -3 hour)>'2014-12-17'");
x=0
for text,coor,dat in cursor:
    if(ifAccidente(text)>=2 and coor!="0|0"):
        print text,dat
        x=x+1
print x
