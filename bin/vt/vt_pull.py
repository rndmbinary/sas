import requests,json

try:
    hash = input('Paste MD5, SHA-1 or SHA-256 here: ')
    json_config = open("../../config/apikeys.conf", 'r')
    json_data = json.load(json_config)
    json_config.close()
except:
    print('Please rerun as one of the two recieved and error')


url = 'https://www.virustotal.com/vtapi/v2/file/download'
params = {
        'apikey': json_data['apikeys'][0]['virustotal'],
        'hash': hash
        }

response = requests.get(url, params=params)

result = open('./'+hash, 'wb')
result.write(response.content)
result.close()

