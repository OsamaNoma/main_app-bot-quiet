from binance.client import Client
import requests
from database import Status
import datetime as dt
import json
import time
import time_server as ts
import binance.client



while True:
 Pkey = 'Rwiro5P8sM3T1lFvq08276Edwo9viV8cbxIFqEq4mzzLPC25rVL67Vthj6UVBUNN'
 Skey = 'Mq5UIuIZLxguP7BanbTp0dPdescemXnSjkWPzvlpNFcWRJMPzr4z78ECyzWLKtDQ'

 client = Client(api_key=Pkey, api_secret=Skey)

 def time_now():
  time = dt.datetime.now()
  time = time.strftime("%H:%M:%S    //   %d-%m-%Y") #10:42:30   //   01-03-2021
  return time

 x = 0
 y = 0

 while True:
  try:
    stat = Status.find_status(collection = "Status")
    while "ON" in stat:
      ts.server_tm()
      if x == 0:
        y = 0
        print("System activated at :", time_now())
        
        x = x+1

    stat = Status.find_status(collection = "Status")
    if y == 0:
      x = 0
      print("System disactivated at :", time_now())
      y = y+1
  except Exception as e:
    if "HTTPSConnectionPool" in str(e) and connection == "OK":
      print("Connection timeout ...")
      connection = "Error"
      time.sleep(2)
      
      pass     
 time.sleep(2)  
