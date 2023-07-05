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


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': link}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    response = response.json()
    return response['link']


def count_clicks(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'units': '-1', 'unit': 'day', }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    link = input('Enter a link: ')
    token = os.environ['BITLY_TOKEN']
    parsed_link = urlparse(link)
    trimmed_link = f'{parsed_link.netloc}{parsed_link.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{trimmed_link}'
    resp = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    try:
        if resp.ok:
            number_of_clicks = count_clicks(token, trimmed_link)
            script_output = f'\nTotal clicks on {link}:  {number_of_clicks} \n'
        else:
            link = shorten_link(token, link)
            script_output = f'\nShort link: {link} \n'
    except requests.exceptions.HTTPError:
        script_output = (
            "\nThe link you entered is incorrect or API isn't responding\n"
            )
    print(script_output)


if __name__ == '__main__':
    main()
