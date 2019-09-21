import requests 

URL = "https://www.fast2sms.com/dev/bulk"
PARAMS = {'authorization':"<your API token>",'sender_id': "FSTSMS", 'message': "Test SMS - python", 'language': "english", 'route':"p", 'numbers':"<numbers to which you want to send SMS, seperated by , >", 'flash': "1" }

r = requests.get(url = URL, params = PARAMS)

data = r.json()
print r
print data 

