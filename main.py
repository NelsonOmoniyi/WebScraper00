from bs4 import BeautifulSoup
import requests
import time
# html_req = requests.get('https://www.infoplease.com/world/countries').text
# soup = BeautifulSoup(html_req, 'lxml')
# countrys = soup.find_all('div', class_='country-wrapper')
# for country in countrys:
#     country_name = country.find('a', class_='name-anchor').text
#     flag = country.find('img', class_='b-lazy')
#     print(f'''Country name: {country_name}
#      Country Flag: {flag}''')
    # print(f'{country_name}')
# print(countrys)

def find_country():
    html_req = requests.get('http://www.scrapethissite.com/pages/simple/').text
    soup = BeautifulSoup(html_req, 'lxml')
    countrys = soup.find_all('div', class_='col-md-4 country')
    for country in countrys:
        # for index, country in enumerate(countrys):
        country_name = country.find('h3', class_='country-name').text.replace(' ', '')
        capital = country.find('span', class_='country-capital').text
        population = country.find('span', class_='country-population').text
        # with open('/Archive', )
        print(f'Country name:{country_name.strip()}')
        print(f'Capital: {capital}')
        print(f'Population Est: {population}')
        print('-----------------------------------')
# --------------------------------------------------------------------------------------------------------------
#  TO PRINT EACH COUNTRY IN A TEXT FILE
# with open(f'Archive/{index}.txt', 'w') as f:
#     f.write(f'Country name:{country_name.strip()}' \n)
#     f.write(f'Capital: {capital}'\n)
#     f.write(f'Population Est: {population}'\n)
#     f.write('-----------------------------------')
# print(f'File {index} Saved Successfully')
#         --------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    while True:
        find_country()
        wait = 1
        print(f'Waiting for {wait} minutes...')
        time.sleep(wait * 60)
