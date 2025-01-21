from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
driver.get(f'https://www.amazon.in/s?k={query}laptop&ref=nb_sb_noss')

elems = driver.find_elements(By.CLASS_NAME, 'puis-card-container')
print(f"{len(elems)} items Found")
for elem in elems:
    print(elem.text)
# print(elem.get_attribute('outerHTML'))


time.sleep(10)
driver.close()

