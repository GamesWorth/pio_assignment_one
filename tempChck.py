#This Program Should be run on the Pi device at intervals
#   Then get the temp and humidity from the sense
#   store in database with time
#   and check if under 20 degrees
#       at that point push an alert to users phone
#   By Aidan Harris s3691198
from sense_hat import SenseHat

def getSenseData():
    sense = SenseHat()
    temp = sense.get_temperature()
	humd = sense.get_humidity()
    #run function to correct temp for PI cpu temp   
    tempFixed = fixtemp(temp)
    if temp is not None:
        temp = round(temp, 1)
        #TODO log values
        #TODO get time value

def fixTemp(val):
    #TODO correct temp value
    return val