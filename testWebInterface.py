import unittest
import sys
import random
from thermometer import thermometer
# #The class we're testing is above the test class
# sys.path.append('..')
# from webInterface import webi
from webInterface import webi
url = "http://localhost:9091/dbinterract/"


class TestWebStuff(unittest.TestCase):
    
    def test_nothing(self):
        print("test_nothing")
        self.assertTrue(True)
        self.assertFalse(False)

    def test_website_responds(self):
        print("test_website_responds")
        webint = webi(url)
        r = webint.get_any_response()
        self.assertTrue(r,200)
        
        webint = webi(url+"bAduRlNotFound")
        r = webint.get_any_response()
        self.assertTrue(r,404)

    def test_GetAllTherms(self):
        print("test_GetAllTherms")
        webint = webi(url)
        therm_list= webint.get_all_therms()
        # print(f"GetAllTherms...{len(therm_list)} items")
        # for t in therm_list:
        #     print(t['plain_name'])
        self.assertTrue(len(therm_list) > 0)
    
    def test_GetATherm(self):
        # #First make sure we can make a call when there are no matching thermomerters. We'll use this a lot
        webint = webi(url)
        my_therm = webint.get_a_therm(plain_name='NeVer AdD THiS',mac='AA:BB:CC:DD:EE:FF')
        self.assertEqual(my_therm,None)
        
        #Now pull one that's for sure in the DB
        therm_list= webint.get_all_therms()
        q_therm=therm_list[0]
        my_therm = webint.get_a_therm(plain_name=q_therm.plain_name,mac=q_therm.device_mac)
        self.assertEqual(my_therm.device_mac, q_therm.device_mac)

    def test_PostATherm(self):
        print("test_PostATherm")
        webint = webi(url)
        webint.add_thermometer(thermometer("AAAThEErm",'AA:EF:55:EC',False))

    def test_DeleteATherm(self):
        print("test_DeleteATherm")
        rando = {random.randrange(100)}
        webint = webi(url)
        newid  = webint.add_thermometer(thermometer(f"AAAThEErm{rando}",'AA:EF:55:EC',False))
        webint.del_a_therm(thermometer(f"AAAThEErm{rando}",'AA:EF:55:EC',False))

if __name__ == '__main__':
    unittest.main()