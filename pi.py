"""
This is the Raspberry Pi side of the GreenHouse Monitor App.  
It's responsibility is to register individual thermometers with the WebApp
and periodically record the current temperature associated with that 
thermometer to the WebApp via HTTP POST
"""

import webInterface
from datetime import datetime
#import RPi.GPIO as GPIO
from Test import gpiostub as GPIO
from os.path import exists
import calendar
import time
import sys
import os
import json
import signal

# import uuid

#This process will likely be run by cron, scheduled to run on 10 minute intervals, etc,
#let the cron try to start, but abdicate if another is running
def abort_if_another_running():
    mypid = os.getpid()
    plist = []
    for line in os.popen("ps ax | grep python | grep "+__file__+" |grep -v grep | grep -v /bin/sh |grep -v "+str(mypid) ):
        plist.append(line)
    
    if len(plist):
        log_output("abdicating.\n"+str(plist))
        time.sleep(2)
        sys.exit(1)

#Process the Ctrl_C keystroke from shell
#This handler will be registered in the Main below
def sigint_handler(signal, frame):
    log_output('\n\nScript Interrupted by signal, Turning off fans and exiting')
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    sys.exit(0)

def log_output(text):
    time =datetime.now().strftime("%H:%M:%S")
    date =datetime.now().strftime("%m-%d-%Y")
    f= open(os.path.expanduser(data['log_dir']+"/Therms"+date+".log"),"a")
    f.write(time+" "+text+"\n")
    f.close()

#Process the Ctrl_C keystroke from shell
#This handler will be registered in the Main below
def sigint_handler(signal, frame):
    log_output('\n\nScript Interrupted by signal, Turning off fans, lights, and exiting')
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    sys.exit(0)


#Access the thermometer dictionary and read the 'files' associated with each one to 
#determine the current temperature in celcius
def read_temp_celcius(thermometer):
    therm_file = os.path.expanduser(thermometer['path_to_file'])
    if (not exists (therm_file) ):
            raise Exception(f"Can't find file:{thermometer['path_to_file']}") #can't read the file, throw exception
    therm_file = open(therm_file,"r")
    contents = therm_file.read()
    #the contents of the thermostat file will look something like this:
    # e7 00 4b 46 7f ff 0c 10 6b : crc=6b YES
    # e7 00 4b 46 7f ff 0c 10 6b t=14437
    therm_file.close
    temp = int(contents.split("t=")[1])/1000.0
    return(temp) 

#Access the thermometer dictionary and read the 'files' associated with each one to 
#determine the current temperature.  return the temperature in fahrenheit
def read_temp_fahrenheit(thermometer):
    return read_temp_celcius(thermometer) * 1.8 + 32

def refresh_thermometers(therms):
    #iterate through Thermometers
    for thermometer in therms:
        thermometer['therm_temp'] = round(read_temp_fahrenheit(thermometer),2)
        log_output(thermometer['therm_name']+": "+str(thermometer['therm_temp'])+"\n")

def post_to_api(data):
    now_time_epoch = calendar.timegm(datetime.now().timetuple())
    for thermometer in data['therm_details']:

        webint.add_temp({'therm':thermometer["therm_name"],'datetime':now_time_epoch,'ftemp':thermometer['therm_temp']})




##########################  main     #########################

#Open File to read configurations
thermFile=open('Therms.json')
#get a dictionary based on file
data = json.load(thermFile)
data['fan_state_word'] = "off"
data['fan_state'] = 0
#close the file
thermFile.close 

#Say what to do when someone presses Ctrl+C
signal.signal(signal.SIGINT,sigint_handler)
signal.signal(signal.SIGTERM,sigint_handler)
# # print (hex(uuid.getnode()))

    # now_time_epoch = calendar.timegm(datetime.now().timetuple())
    # webint.add_temp({'therm':1,'datetime':now_time_epoch,'ftemp':83.7,})


#abort_if_another_running()
try:
    while(True):
        log_output("Launching Thermostat Control . . .")
        webint = webInterface.webi(data['api_base_url'])
        refresh_thermometers(data['therm_details'])
        post_to_api(data)
        time.sleep(float(data['check_freq_seconds']))

except Exception as ex:
    print(f"Error:{ex}")

finally:
    log_output ("\n\n\n--------------Powering Down GPIO 18,23\n")
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)

print("end")