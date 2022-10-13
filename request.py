import urequests as requests

class SMS :
    def __init__(self):
        self.sender = "Intrusion"
        self.url = "https://sms.arkesel.com/sms/api?action=send-sms"
        self.APIKEY = "OnhkSzhGTWVwaWtnUENlYWs="
    
    def send (self,recipient, message):
        payload ="&api_key={}& to={}&from={}&sms={}".format(self.APIKEY,recipient,self.sender,message)
        url = self.url+payload
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
        return data
    
    def checkBalance():
        pass
    
    def balanceAlert():
        pass
    
    def purchase():
        pass
    



if __name__ == "__main__":
    '''response = requests.get("https://sms.arkesel.com/sms/api?action=send-sms&api_key=OnhkSzhGTWVwaWtnUENlYWs=& to=0554317909&from=Me&sms=hello")'''
    sms1 = SMS()
    test = sms1.send("0554317909", "Intruder detected1")
    print(test)
