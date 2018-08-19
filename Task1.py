#!/usr/bin/python3
#This Program Should be run on the Pi device at intervals
#   when run get the temp and humidity from the sense
#   store in database with timestamp
#   By Aidan Harris s3691198

from sense_hat import SenseHat
import datetime
import sqlite3
import logging
import os

#logging.basicConfig(level=logging.DEBUG)
dbname='/home/pi/Assignment_1/sensehat.db'#database to store logged data
factor = 1.5 #value for temp correction


#insert readings into database /code from weekly pracs
def logData(time,humd,temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values((?),(?),(?))", (time,temp,humd))
    conn.commit()
    conn.close()
    print("Inserted data into db")
    displayData()


# display database data
def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
    conn.close()

def getTimeStamp():
    time = datetime.datetime.now()
    #<---if any adjustmants to time format are needed put here<---
    return time   

#get temp of cpu to correct sensehat readings code based on http://yaab-arduino.blogspot.com/2016/08/accurate-temperature-reading-sensehat.html
def getCpuTemp():
    cpuT = os.popen("vcgencmd measure_temp").readline()
    val = float(cpuT.replace("temp=","").replace("'C\n",""))
    return(val)

#fix temp according to cpu
def fixTemp(val):
    cpu_temp = getCpuTemp()
    logging.debug("CPU temp is %d"% cpu_temp)
    logging.debug("Sense temp is %d"% val)
    val = val - ((cpu_temp - val)/factor)
    logging.debug("corrected temp is %d"% val)
    return val

def getSenseData():
    sense = SenseHat()
    temp = sense.get_temperature()
    humd = sense.get_humidity()
    tempFixed = fixTemp(temp)#run function to correct temp for Pi cpu temp   
    if temp is not None:
        tempFixed = round(tempFixed, 3)
        humd = round(humd, 3)
        time = getTimeStamp()
        logData(time,humd,tempFixed)

def main():
    getSenseData()

main()