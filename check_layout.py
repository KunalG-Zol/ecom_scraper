from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.flipkart.com'
search_query = input("Type the search query:")
driver = webdriver.Firefox()
driver.get(url)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="Pke_EE"]')))
search_box = driver.find_element(By.XPATH, '//input[@class="Pke_EE"]')
search_box.send_keys(search_query, Keys.ENTER)


def CheckLayout():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._1AtVbE.col-12-12')))
    full_length_prod = driver.find_element(By.CSS_SELECTOR, 'div._13oc-S')
    try:
        full_length_prod.find_element(By.CSS_SELECTOR, 'div[data-id][style*="100"]')
        full_length = True
    except:
        full_length = False

driver.quit()
