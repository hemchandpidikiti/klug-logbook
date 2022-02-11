import requests
pload = {'username':'180030375','password':'Starz&1a'}
r = requests.post('http://95.217.217.134:2824/auth/',data = pload)
print(r.text)
url='http://95.217.217.134:2824/api/master/mget/'
payload = {
    "rfid_id" : "6887218235"
    #"
    }
headers={"Authorization" : "Token fe4463f5170d2c8e8bec72e870483b7eeea03a12"}
r = requests.post(url, data=payload, headers=headers)
print(r.content)

