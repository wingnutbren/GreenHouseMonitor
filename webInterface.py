import requests
import json
from thermometer import thermometer

class webi:
    baseurl = ""
    csrftoken = "DEF"
    client = requests.session()

    def __init__(self, baseurl) -> None:
        self.baseurl = baseurl
        c=self.client
        #make an http get to retrieve cross site request forgery token

        c.get(baseurl+"AllTherms")
        if 'csrftoken' in c.cookies:
            self.crsftoken = c.cookies['csrftoken']
        else:
            self.crsftoken = c.cookies['csrf']

    def add_temp (self,payload):
        #Post
        payload["csrfmiddlewaretoken"]=self.crsftoken
        r = self.client.post(self.baseurl+"AddTemps",payload)
        # print(r.text)

    def add_thermometer(self,payload):
        #Post
        payload["csrfmiddlewaretoken"]=self.crsftoken
        r = self.client.post(self.baseurl+"AddTherm",payload)
        # print(r.text)

    def get_a_therm(self,mac,plain_name):
        #Get
        rj = self.client.get(self.baseurl+"ATherm",params={ 'mac' : mac, 'plain_name' : plain_name })
        r = dict()
        r = rj.json()
        if('noresults' in r.keys()):
            return None
        else:
            return thermometer(r['plain_name'],r['mac'],False)        


    def get_all_therms(self):
        #Get
        r = self.client.get(self.baseurl+"AllTherms?json=true")
                # print(f"GetAllTherms...{len(therm_list)} items")
        result_list = r.json()
        therm_list=list()
        for t in result_list:
            th = thermometer(t['plain_name'],t['device_mac'],False)
            
                # plt['plain_name'],t.['device_mac'])
            therm_list.append( th )
        return therm_list
        
        # therms = json.loads(json.loads(r.text))
        # return therms
 
        

    #Used for testing. Make sure the URL answers
    def get_any_response(self):
       r = self.client.get(self.baseurl)
       
        

        



