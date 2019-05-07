'''
    NAME: AutoFocus Query
    AUTHOR: TYRON HOWARD
    VER: 0.9
    DESC: This is part of suite of python tools that will query the AutoFoucs API
'''
import requests,json

try:
    hash = input('Paste MD5: ')
    json_config = open("../config/apikeys.conf", 'r')
    json_data = json.load(json_config)
    json_config.close()
except:
    print('Please rerun as one of the two recieved and error')

#Paramiters For AutoFocus query
params = {
        'apiKey': json_data['apikeys'][0]['autofocus'],
        'query': {
            'operator': 'all',
            'children': [ 
                {
                 'field': 'sample.md5',
                 'operator': 'is',
                 'value': hash
                },
            ]
        },
        'size': 50,
        'from': 0,
        'sort' : {
            'create_date' : {
                'order': 'desc'
            }
        },
        'scope': 'public'
        }

# Pull API Key from Params
for k,v in params.items():
    if k == "apiKey" :
        apikey_json = {k:v}
        break

#Required to Request information from AutoFocus
url_query = 'https://autofocus.paloaltonetworks.com/api/v1.0'
headers = { "content-type": "application/json" }
search_query = '/samples/search/'
results_query = '/samples/results/'
sessions_query = '/sessions/results/'

# Search Query and Response (Debating if this is still needed)
response = requests.post(url_query + search_query, headers=headers, json=params).json()
print(response)
# TESTING:  print(params['apiKey'] + " job hash ---->  %s" % response['af_cookie']) 

# Use API key to pull Sample results.
samples_results = requests.post(url_query + results_query + response['af_cookie'], headers=headers, json=apikey_json).json()

# Use API key to pull Sessions results.
sessions_results = requests.post(url_query + sessions_query + response['af_cookie'], headers=headers, json=apikey_json).json()

# Samples_Results and sha256 is required for pulling Analysis results.
sha256 = samples_results['hits'][0]['_source']['sha256']
analysis_query = '/sample/%s/analysis' % sha256

# Use API key to pull Analysis results.
analysis_results = requests.post(url_query + analysis_query, headers=headers, json=apikey_json).json()

# Put all results in one varible to print. (Lazy)
results = samples_results, sessions_results, analysis_results

# Save Results to Disk
analysis_sha256 = open('./' + sha256 +'.txt', 'a')
analysis_sha256.write(str(json.dumps(results, indent=2)))
analysis_sha256.close()
