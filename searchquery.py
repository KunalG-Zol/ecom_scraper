from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.flipkart.com'


driver = webdriver.Firefox()
driver.get(url)
search_query = input("Type the search query:")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="Pke_EE"]')))
search_box = driver.find_element(By.XPATH, '//input[@class="Pke_EE"]')
search_box.send_keys(search_query, Keys.DOWN, Keys.ENTER)
