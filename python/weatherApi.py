import json
import requests, re


print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=abff08e92bdddcf004db4456aadf9bdf' % zip)
data=r.json()
print(data['weather'][0]['description'])