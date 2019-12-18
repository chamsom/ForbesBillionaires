import urllib
import urllib.request
from bs4 import BeautifulSoup
import csv


def make_soup(url):
    forbes = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(forbes, 'html.parser')
    return soupdata


soup = make_soup('https://www.forbes.com/profile/sheldon-adelson/?list=billionaires#d4342084a224')
soup.get_text(strip = True)

for profile in soup.findAll('div', {'class': 'profile-content'}):

    for name in soup.findAll('div', {'class': 'profile-heading--desktop'}):
        richnames = name.h1.text
        richowner = name.div.text
    print(richnames + ': ' + richowner)

    for info in soup.findAll('div', {'class': 'profile-info'}):
        worth = soup.find('div', {'class': 'profile-info__item-value'}).text
        print('Net Worth: ' + worth)

    for stats in soup.findAll('div', {'class': 'profile-stats__item'}):
        print(stats.text)

with open('Forbes.csv', 'w') as r:
    for profile in soup.findAll('div', {'class': 'profile-content'}):

        for name in soup.findAll('div', {'class': 'profile-heading--desktop'}):
            richnames = name.h1.text
            richowner = name.div.text
        r.write(richnames + ': ' + richowner + '\n')

        for info in soup.findAll('div', {'class': 'profile-info'}):
            worth = soup.find('div', {'class': 'profile-info__item-value'}).text
        r.write('Net Worth: ' + worth + '\n')

        for stats in soup.findAll('div', {'class': 'profile-stats'}):

            for title in soup.findAll('span', {'class': 'profile-stats__title'}):
                r.write(title.text + ': ' + '\n')

            # for p in soup.findAll('span', {'class': 'profile-stats__text'}):
            #     r.write(p.text)



            # r.write(stats.text + '\n')
