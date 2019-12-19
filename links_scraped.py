# developing idea for obtaining the next links for pagination
# identified class containing the href for the "Next" button on Forbes
# this is just a test file at the moment...

import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'chamsom' + 'anranwang4',
    'From': 'https://github.com/chamsom' + 'https://github.com/anranwang4'
}

url = 'https://github.com/chamsom' + 'https://github.com/anranwang4'

page = requests.get(url, headers = headers)

def make_soup(url):
    forbes = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(forbes, 'html.parser')
    return soupdata

soup = make_soup('https://www.forbes.com/profile/sheldon-adelson/?list=billionaires#d4342084a224')
for link in soup.findAll(attrs = {'class': 'profile-nav__next'}):
    page_url = 'forbes.com'
    print(page_url + link.get('href'))

# link = soup.find(attrs = {'class': 'profile-nav__next'})
# print(link.get('href'))