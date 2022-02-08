from blockchain_utilities import http_get, import_JSON_dict
import requests
url = 'http://cat:5000'
request_url = url+'/head'
head_hash = http_get(request_url).content

request_url = url + '/fetch/' + head_hash.decode()

request_content = http_get(request_url).content.decode()
chat_dict = import_JSON_dict(request_content,'text')
print(chat_dict['payload'])
