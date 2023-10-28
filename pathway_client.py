import requests
import re
import os

data = {"user": "user", "query": "How to  directory named dir"}

post_response = requests.post("http://localhost:8080/", json=data)

post_response_json = post_response.json()

print(post_response_json)


import re

text = post_response_json

m = re.search('^(.*), you can use the command "(.*)".', text)
if m:
    found = m.group(2)
    os.system(found)
