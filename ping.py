import requests
import json

params = {
  'api_key': 'c78bbb29-56b2-4347-9d89-fd3e72238896',
  'params1': 'value1'
}
method = 'ping'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()

print(json.dumps(api_response, indent=4, sort_keys=True))