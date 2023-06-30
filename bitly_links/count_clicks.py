#!/usr/bin/python3
"""
The script turns long links into shortend links like 
ex. https://www.google.com/search?q=how+to+be+cool 
=> https://bit.ly/46lV7aP
If the link already exists, the script returns how many times people 
clicked on it:
ex. Total clicks on https://bit.ly/46lV7aP:  11

"""

import os
from urllib.parse import urlparse
import requests

token = os.getenv('BITLY_TOKEN')


def shorten_link(token, url):
    target_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    payload = {'long_url': url}
    response = requests.post(target_url, headers=headers, json=payload)
    response.raise_for_status()
    response = response.json()
    return response['link']


def count_clicks(token, bitlink):
    bitlink = bitlink.replace('http://', '').replace('https://', '')
    headers = {'Authorization': 'Bearer {}'.format(token)}
    params = {'units': '-1', 'unit': 'day', }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    link = input('Enter a link: ')
    parsed = urlparse(link)
    full_path = (
        f'https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}/{parsed.path}'
    )
    resp = requests.get(full_path, headers={'Authorization': f'Bearer {token}'})
    try:
        if resp.ok:
            print(link)
            number_of_clicks = count_clicks(token, link)
            result = f'\nTotal clicks on {link}:  {number_of_clicks} \n'
        else:
            link = shorten_link(token, link)
            result = f'\n Short link: {link} \n'
    except requests.exceptions.HTTPError:
        result = "\nThe link you entered is incorrect or API isn't responding"
    print(result)


if __name__ == '__main__':
    main()
