#This Program Should be run on the Pi device at intervals
#   when run get the temp and humidity from the sense
#   store in database with timestamp
#   By Aidan Harris s3691198

from sense_hat import SenseHat
import datetime
import sqlite3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
dbname='senseData.db'#database to store logged data
factor = 1.5 #value for temp correction


#insert readings into database
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

def getCpuTemp():
    cpuT = os.popen("vcgencmd measure_temp").readline()
    val = float(cpuT.replace("temp=","").replace("'C\n",""))
    return(val)

#fix temp according to cpu
def fixTemp(val):
    cpu_temp = getCpuTemp()
    val = val - ((cpu_temp - val)/factor)
    return val

def getSenseData():
    sense = SenseHat()
    temp = sense.get_temperature()
    humd = sense.get_humidity()
    tempFixed = fixTemp(temp)#run function to correct temp for Pi cpu temp   
    if temp is not None:
        tempFixed = round(tempFixed, 3)
        humd = round(humd, 3)
        time = getTimeStamp
        logData(time,humd,temp)

def main():
    getSenseData()

main()