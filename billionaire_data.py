import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    forbes = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(forbes, 'html.parser')
    return soupdata

soup = make_soup('https://www.forbes.com/profile/sheldon-adelson/?list=billionaires#d4342084a224')

for profile in soup.findAll('div', {'class': 'profile-content'}):

    for name in soup.findAll('div', {'class': 'profile-heading--desktop'}):
        richnames = name.h1.text
        richowner = name.div.text
    print(richnames + ': ' + richowner)

    for info in soup.findAll('div', {'class': 'profile-info'}):
        worth = soup.find('div', {'class': 'profile-info__item-value'}).text
        print('Net Worth: ' + worth)

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

            title = soup.find_all(attrs={'class': "profile-stats__title"})
            title_info = soup.find_all(attrs={'class': "profile-stats__text"})

            for title, title_info in zip(title, title_info): # who knew that zip would come in clutch from Dr. Putonti?
                r.write(title.getText() + ',' + title_info.getText() + '\n')

            # for title in soup.findAll('span', {'class': 'profile-stats__title'}): DISCONTINUED LOOPS SINCE THIS BEHAVES LIKE GARBO
            #     new_title = title.text
            #     r.write(new_title + ': ' + '\n')
            #
            #
            # for p in soup.findAll('span', {'class': 'profile-stats__text'}):
            #     new_p = p.text
