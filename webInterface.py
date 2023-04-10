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

        c.get(baseurl)
        if 'csrftoken' in c.cookies:
            self.csrftoken = c.cookies['csrftoken']
        else:
            self.csrftoken = c.cookies['csrf']

    def add_temp (self,payload):
        #Post
        payload["csrfmiddlewaretoken"]=self.csrftoken
        r = self.client.post(self.baseurl+"AddTemp",payload)

    def add_thermometer(self,therm:thermometer):
        #Post
        payload = therm.as_payload_dict()
        payload["csrfmiddlewaretoken"]=self.csrftoken
        payload["json"]="true"

        r = self.client.post(self.baseurl+"AddTherm",payload)
        id_dict = r.json()
        return id_dict['id']

    def get_a_therm(self,mac,plain_name):
        #Get
        rj = self.client.get(self.baseurl+"ATherm",params={ 'mac' : mac, 'plain_name' : plain_name })
        therm = rj.json()
        if('noresults' in therm.keys()):
            return None
        else:
            t=thermometer(therm['plain_name'],therm['mac'],False)  
            t.id = therm['id']    
            return t

    def del_a_therm(self,therm: thermometer):
        data={'csrfmiddlewaretoken':self.csrftoken}
        url = self.baseurl+f"DeleteThermByNameMac/{therm.plain_name}/{therm.device_mac}"
        self.client.post(url, data=data, headers= {'Referer': url})
        

    def get_all_therms(self):
        #Get
        r = self.client.get(self.baseurl+"AllTherms?json=true")
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
       return r.status_code
       
        

        



