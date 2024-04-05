from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com'
search_query = "ps4 games"

driver = webdriver.Firefox()
driver.get(url)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="Pke_EE"]')))
search_box = driver.find_element(By.XPATH, '//input[@class="Pke_EE"]')
search_box.send_keys(search_query, Keys.DOWN, Keys.ENTER)

# Wait until the link tag is present in the DOM
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "link[rel='stylesheet'][href*='e82689']")))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "link[rel='stylesheet'][href*='b2aeab']")))

# Find the link tag with the given CSS selector
css_link1 = driver.find_element(By.CSS_SELECTOR, 'link[rel="stylesheet"][href*="e82689"]')
css_link2 = driver.find_element(By.CSS_SELECTOR, 'link[rel="stylesheet"][href*="b2aeab"]')
css_url1 = css_link1.get_attribute('href')
css_url2 = css_link2.get_attribute('href')

# Get the CSS file content
css_response1 = requests.get(css_url1)
css_response2 = requests.get(css_url2)

css_content1 = css_response1.text
css_content2 = css_response2.text

css_rules1 = css_content1.split("}")
css_rules2 = css_content2.split("}")
price_class = None

for rule in css_rules1:
    if "display:inline-block;font-size:16px;font-weight:500;color:#212121" in rule:
        price_class = rule.split("{")[0].split(" ")[0].strip(".")
        break

print(price_class)

driver.quit()