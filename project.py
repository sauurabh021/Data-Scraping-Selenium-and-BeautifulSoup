from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file_num = 0
for i in range(2, 20):
    driver.get(f"https://www.amazon.in/s?k={query}laptop&page={i}&crid=1JAAHX169JR28&qid=1731444762&sprefix=%2Caps%2C877&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, 'puis-card-container')
    print(f"{len(elems)} items Found")

    for elem in elems:
        d = elem.get_attribute('outerHTML')
        with open(f"data/{query}{file_num}.txt", "w", encoding="utf-8") as f:
            f.write(d)
    file_num += 1

                # print(elem.text)
            # print(elem.get_attribute('outerHTML'))


time.sleep(10)
driver.close()

