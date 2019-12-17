import urllib
import urllib.request
import csv
from bs4 import BeautifulSoup


def make_soup(url):
    forbes = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(forbes, 'html.parser')
    return soupdata

soup = make_soup('https://www.forbes.com/profile/sheldon-adelson/?list=billionaires#d4342084a224')
# for stats in soup.findAll('div', {'class':'profile-stats__item'}): testing purposes ignore line
#     print(stats.find('span').text)

for profile in soup.findAll('div', {'class':'profile-content'}):

    for name in soup.findAll('div', {'class':'profile-heading--desktop'}):
        richnames = name.h1.text
        richowner = name.div.text
    print(richnames + ': ' + richowner)

    for info in soup.findAll('div', {'class':'profile-info'}):
        worth = soup.find('div', {'class':'profile-info__item-value'}).text
        print('Net Worth: ' + worth)

    for stats in soup.findAll('div', {'class':'profile-stats__item'}):
        print(stats.text)

    # for profile_stats in soup.findAll('span', {'class':'profile-stats__title'}):
    #     print(profile_stats.text)


    # profile_stats = soup.find('div', {'class':'profile-stats__item'}).text
    # print(profile_stats)

