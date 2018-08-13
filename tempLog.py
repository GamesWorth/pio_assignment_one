#This Program Should be run on the Pi device at intervals
#   Then get the temp and humidity from the sense
#   store in database with time
#   By Aidan Harris s3691198
from sense_hat import SenseHat
import datetime
import sqlite3

dbname='senseData.db'#database to store logged data

def logData(time,humd,temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values((?),(?),(?))", (time,humd,temp))
    conn.commit()
    conn.close()

def getTimeStamp():
    time = datetime.datetime.now()
    #<---if any adjustmants to time format are needed put here<---
    return time   

def fixTemp(val):
    #TODO correct temp value
    return val

def getSenseData():
    sense = SenseHat()
    temp = sense.get_temperature()
    humd = sense.get_humidity()
    tempFixed = fixTemp(temp)#run function to correct temp for PI cpu temp   
    if temp is not None:
        tempFixed = round(tempFixed, 3)
        humd = round(humd, 3)
        time = getTimeStamp
        logData(time,humd,temp)

   


