from blockchain_utilities import http_get, import_JSON_dict
import requests

URL = 'http://cat:5000'

# Build the request URL and retrieve the head block's hash
request_url = URL+'/head'
head_hash = http_get(request_url).content

# Buid the URL  and retrieve the block with the hash we just recieved
request_url = URL + '/fetch/' + head_hash.decode()
request_content = http_get(request_url).content.decode()

# convert the block from JSON to usable Python format (a dict)
chat_dict = import_JSON_dict(request_content,'text')
print(chat_dict.keys())
