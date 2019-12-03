import serial
import struct
import requests
import json
import requests


URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId,
  }
  return requests.post(reqUrl, req_params)

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0,1]
while True:
    read_serial=ser.readline()
    a=read_serial.split()
    b=a[0]
    z=float(b)
    print(z)
    if(z<40.0):
        
        response = sendPostRequest(URL, 'Enter_your_Api_Key_here', 'Enter_your_secret_key_here', 'stage', 'Enter_your_phone_number', 'Alarsh', 'Water level low , Need water' )
        print ( response.text)
    
    
    
    
    
import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


