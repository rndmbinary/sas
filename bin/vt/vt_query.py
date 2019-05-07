import requests,json

try:
    apikey = input('Paste API Key here: ')
    hash = input('Paste MD5, SHA-1 or SHA-256 here: ')
except:
    print('Please rerun as one of the two recieved and error')


url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {
        'apikey': apikey, 
        'resource': hash,
        'allinfo': 'true'
        }
response = requests.get(url, params=params)

result = json.dumps(response.json())

print(result)

