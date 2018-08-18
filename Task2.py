#this program will check the temperature and send a push bullet notification to the phone
#   get temp from sensehat
#   check if temp value is under 20 degrees
#   send message to pushbullet app
#by Aidan Harris s3691198

#!/usr/bin/env python3
from sense_hat import SenseHat
import requests
import json
import os
import logging #used to test functionality on pi OS
import subprocess

ACCESS_TOKEN="o.tzyK4MLO5kfz6g34TZ9iWIgEpO9OBE0n"
logging.basicConfig(level=logging.DEBUG)
threshold = 20 #threshold for when to send an alert

#Function will send notification/ used from weekly practicals code
def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#get temp of cpu to correct sensehat readings
def getCpuTemp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)

#fix temp according to cpu
def fixTemp(val):
    #TODO copy function from task 1 when complete
    cpu_temp = getCpuTemp()
    logging.debug("CPU temp is %d"% cpu_temp)
    logging.debug("Sense temp is %d"% val)
    val = val - ((cpu_temp - val)/5.466)
    logging.debug("corrected temp is %d"% val)
    return val

#get temp from sensehat
def getTemp():
    sense = SenseHat()
    temp = sense.get_temperature()
    if temp is not None:
        temp = fixTemp(temp)
        return temp

#main function
def main():
    temp = getTemp()
    if temp < threshold:
        logging.debug("Detected under temp threshold")
        formatTemp = round(temp,1)
        mssg = ("The temperature is currently %d degrees, you might want to grab a jumper."% formatTemp)
        send_notification_via_pushbullet("It is cold", mssg)
    else:
        logging.debug("Detected Above Temp threshold")

#Execute program
main()
