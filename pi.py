"""
This is the Raspberry Pi side of the GreenHouse Monitor App.  
It's responsibility is to register individual thermometers with the WebApp
and periodically record the current temperature associated with that 
thermometer to the WebApp via HTTP POST
"""

import webInterface
from collections import namedtuple
from datetime import datetime
import calendar
# import uuid

baseurl="http://localhost:9091/dbinterract/"  #TODO: get this from json config

webint = webInterface.webi(baseurl)

# print (hex(uuid.getnode()))
now_time_epoch = calendar.timegm(datetime.now().timetuple())
webint.add_temp({'therm':1,'datetime':now_time_epoch,'ftemp':83.7,})

