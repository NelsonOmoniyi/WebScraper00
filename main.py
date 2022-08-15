from bs4 import BeautifulSoup
import requests

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


html_req = requests.get('http://www.scrapethissite.com/pages/simple/').text
soup = BeautifulSoup(html_req, 'lxml')
countrys = soup.find_all('div', class_='col-md-4 country')
for country in countrys:
    country_name = country.find('h3', class_='country-name').text.replace(' ','')
    capital = country.find('span', class_='country-capital').text
    population = country.find('span', class_='country-population').text
    print(f'''Country name:{country_name}
     Capital: {capital} 
     Population Est: {population}''')



