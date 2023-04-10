class thermometer:
    plain_name = ''
    device_mac = ''
    device_lat = 0
    device_lon = 0
    device_ele = 0

    #client only
    monitor_me = False
    temp_max = 0
    temp_min = 0
    in_db = False
    id = None
    current_temp = 0
    path_to_file = None

    def __init__(self,plain_name,device_mac,monitor_me):
        self.plain_name = plain_name
        self.monitor_me = monitor_me
        self.device_mac = device_mac

    def as_payload_dict(self):
        pl = dict()
        pl['plain_name']= self.plain_name
        pl['device_mac'] = self.device_mac
        pl['device_lat'] = self.device_lat
        pl['device_lon'] = self.device_lon
        pl['device_ele'] = self.device_ele
        return pl



        

