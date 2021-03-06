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

with open('Forbes.csv', 'w') as r:
    for profile in soup.findAll('div', {'class': 'profile-content'}):

        for name in soup.findAll('div', {'class': 'profile-heading--desktop'}):
            richnames = name.h1.text
            richowner = name.div.text
        r.write(richnames + ',' + richowner + '\n')

        for info in soup.findAll('div', {'class': 'profile-info'}):
            worth = soup.find('div', {'class': 'profile-info__item-value'}).text
        r.write('Net Worth' + ',' + worth + '\n')

        for stats in soup.findAll('div', {'class': 'profile-stats'}):

            title = soup.find_all(attrs = {'class': "profile-stats__title"})
            title_info = soup.find_all(attrs = {'class': "profile-stats__text"})

            for title, title_info in zip(title, title_info): # who knew that zip would come in clutch from Dr. Putonti?
                r.write(title.getText() + ',' + title_info.getText() + '\n')
