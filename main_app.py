from binance_client import client
import requests
from database import Status
import datetime as dt
import json
import time
import time_server as ts
 


def time_now():
  time = dt.datetime.now()
  time = time.strftime("%H:%M:%S    //   %d-%m-%Y") #10:42:30   //   01-03-2021
  return time

x = 0
y = 0

while True:
  #try:
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
  #except Exception as e:
    #if "HTTPSConnectionPool" in str(e) and connection == "OK":
      #print("Connection timeout ...")
      #connection = "Error"
      #time.sleep(2)
      
      #pass     

    time.sleep(2)  
if __name__ == '__main__':
      main() 