import requests, json
import os

token = os.getenv("TOKEN")


def count_clicks(token, bitlink):
  bitlink = bitlink.replace("http://","").replace("https://","")
  headers = {"Authorization": "Bearer {}".format(token)}
  params = {'units':'-1','unit':'day',}
  url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
  response = requests.get(url, headers=headers, params=params)
  response.raise_for_status()
  return(response.json()['total_clicks'])


def shorten_link(token, url):
  target_url = 'https://api-ssl.bitly.com/v4/shorten'
  headers = {"Authorization": "Bearer {}".format(token)}
  payload = {"long_url": url}
  response = requests.post(target_url, headers=headers, json=payload)
  response.raise_for_status()
  response_json = response.json()
  return(response_json['link'])

def main():
  link=input("Enter a link: ")
  try:
    if link.startswith(("http://bit.ly/","https://bit.ly")):
      number_of_clicks = count_clicks(token, link)
      result = "\n Total clicks on {}:  {} \n".format(link, number_of_clicks)
    else:
      link=shorten_link(token, link)
      result = "\n" + link + "\n"
  except requests.exceptions.HTTPError:
      result = "\n The link you entered is incorrect\n"
  print(result)


if __name__ == '__main__':
  main()