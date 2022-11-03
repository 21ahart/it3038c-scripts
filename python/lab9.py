import json
import requests, re

r = requests.get('http://localhost:3000')
data = r.json()
for i in range(len(data)):
    name = str(data[i]["name"])
    color = str(data[i]["color"])
    print( str(name) + " is " + str(color) + ".") 