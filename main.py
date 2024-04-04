import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

data = {'Title': [], 'Price': [], 'Link': [], 'Rating': []}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://www.flipkart.com/search?q=ps4+games&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=ps4+games&requestId=aac89243-ba16-4a34-970a-a87cc551131d'


response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

game_link = soup.select('a._2rpwqI')

game_block = soup.find_all('div', class_='_4ddWXP')

for rating_raw in game_block:
    rating = rating_raw.select_one('div._3LWZlK')
    if rating:
        data['Rating'].append(rating.text)
        # print(rating.text)
    else:
        data['Rating'].append('None')
        # print('None')

for links in game_link:
    link = links.get('href')
    data['Link'].append('https://flipkart.com'+link)


titles = soup.select('a.s1Q9rs')

for prices in game_block:
    price = prices.select_one('div._30jeq3')
    data['Price'].append(price.string)
for title in titles:
    data['Title'].append(title.string)






dframe = pd.DataFrame.from_dict(data)
dframe.to_csv('data.csv', index=False)
dframe.to_excel('data.xlsx', index=False)

# print(len(data['Title']))
# print(len(data['Price']))
# print(len(data['Link']))
# print(len(data['Rating']))