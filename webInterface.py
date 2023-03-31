import requests
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
        print(r.text)

    def pull_therms(self,mac,thermid):
        ...

        



