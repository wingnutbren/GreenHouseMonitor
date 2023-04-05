class thermometer:
    plain_name = ''
    device_mac = ''
    device_lat = 0
    device_lon = 0
    device_ele = 0
    monitor_me = False
    temp_max = 0
    temp_min = 0
    in_db = False

    def __init__(self,plain_name,device_mac,monitor_me):
        self.plain_name = plain_name
        self.monitor_me = monitor_me
        self.device_mac = device_mac

    # def __init__(self,plain_name,monitor_me,temp_max, temp_min, device_mac, device_lat, device_lon):
    #     super(plain_name,monitor_me)
    #     self.temp_max = temp_max
    #     self.temp_min = temp_min
    #     self.device_mac = device_mac
    #     self.device_lat = device_lat
    #     self.device_lon = device_lon

    def add_to_api(webbi):
        in_db = True


        

