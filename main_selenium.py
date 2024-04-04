from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

search_query = input("Type the search query:")
pages_to_scrape = int(input("Enter the number of pages to extract:"))

url = 'https://www.flipkart.com'

driver = webdriver.Firefox()
driver.get(url)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="Pke_EE"]')))
search_box = driver.find_element(By.XPATH, '//input[@class="Pke_EE"]')
search_box.send_keys(search_query, Keys.ENTER)
data = {'Title': [], 'Price': [], 'Link': [], 'Rating': []}
while True:
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='_4ddWXP')
    links = soup.select('a._2rpwqI')

    for rating_raw in blocks:
        rating = rating_raw.select_one('div._3LWZlK')
        if rating:
            data['Rating'].append(rating.text)
            # print(rating.text)
        else:
            data['Rating'].append('None')
            # print('None')

    for links in links:
        link = links.get('href')
        data['Link'].append('https://flipkart.com' + link)

    titles = soup.select('a.s1Q9rs')

    for prices in blocks:
        price = prices.select_one('div._30jeq3')
        if price:
            data['Price'].append(price.text)
            # print(rating.text)
        else:
            data['Price'].append('None')
    for title in titles:
        data['Title'].append(title.string.title())

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Page")]')))
    page_info_element = driver.find_element(By.XPATH, '//span[contains(text(),"Page")]')
    page_info = page_info_element.text.split('of ')
    current_page = int(page_info[0].split(' ')[1])
    last_page = int(page_info[1])
    print(current_page, last_page)
    try:

        if current_page >= last_page or current_page >= pages_to_scrape:
            break

        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="_1XXPTY._1v2cG7"]')))
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="_1LKTO3"]//span[contains(text(), "Next")]')))
        next_button.click()
    except Exception as e:
        print("Error:", e)

driver.quit()
csv_name = input("Enter the name of the csv file to write to:")
excel_name = input("Enter the name of the excel file to write to:")

dframe = pd.DataFrame.from_dict(data)
dframe.to_csv(csv_name, index=False, encoding='utf-8')
dframe.to_excel(excel_name, index=False)

# print(len(data['Title']))
# print(len(data['Price']))
# print(len(data['Link']))
# print(len(data['Rating']))
