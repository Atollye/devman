#!/usr/bin/env python
import requests

params = {
		 'lang':'ru', 'n':'', 'T':'','m':'','q':''
		}

for place in ['Лондон', 'Шереметьево', 'Череповец']:
    response = requests.get( 'https://wttr.in/{}'.format(place), params=params )

print(response.text)
