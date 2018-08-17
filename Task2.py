#this program will check the temperature and send a push bullet notification to the phone
#   get temp from sensehat
#   check if temp value is under 20 degrees
#   send message to pushbullet app
#by Aidan Harris s3691198

#!/usr/bin/env python3
import requests
import json
import os

ACCESS_TOKEN="o.tzyK4MLO5kfz6g34TZ9iWIgEpO9OBE0n"
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
#fix temp according to cpu
def fixTemp(val):
    #TODO copy function from task 1 when complete
    return val
#get temp from sensehat
def getTemp():
    sense = SenseHat()
    temp = sense.get_temperature()
    temp = fixTemp(temp)
    return temp
#main function
def main():
    temp = getTemp()
    if(temp<20)
        fTemp = round(temp,1)
        mssg = ("It is currently %d degrees, you might want to grab a jumper.")
        send_notification_via_pushbullet("It is cold", mssg)

#Execute
main()
