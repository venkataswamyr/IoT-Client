import requests
from xmlUserMethods import xmlConstructLoad

def UpdateXMSLoad(UID, Pin, ControlValue):
    xml = xmlConstructLoad(str(ControlValue))
    headers = {'Content-Type': 'application/xml'}
    return requests.post('https://openioe.herokuapp.com/api/updatexml/'+str(UID)+'/'+str(Pin), data=xml, headers=headers).text
