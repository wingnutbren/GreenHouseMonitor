import os
import time
from datetime import datetime
from random import randrange
def rewriteFile(path):
    therm_file = os.path.expanduser(path)
    f = open(therm_file,"r")
    contents = f.read()
    #the contenm_filets of the thermostat file will look something like this:
    # e7 00 4b 46 7f ff 0c 10 6b : crc=6b YES
    # e7 00 4b 46 7f ff 0c 10 6b t=14437
    f.close

    #Grab the prefix and the temp, change the temp a little
    splits = contents.split("t=")
    temp = int(splits[1])
    temp += randrange(-1000,1100)
    print(f"{datetime.now()}:  NewTemp: {temp}")
    # #re-write the file
    f = open(therm_file,"w")
    f.write(splits[0]+f"t={temp}")
    f.close

while(True):
    rewriteFile("~/GreenHouseFakeData/w1_slave")
    rewriteFile("~/GreenHouseFakeData/w2_slave")
    time.sleep(50)

