from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
driver.get(f"https://www.amazon.in/Dell-Smartchoice-G15-5530-Gaming-i5-{query}13450HX/dp/B0CRKXDX83/ref=sr_1_1_sspa?crid=1YN16ZC2R13OR&dib=eyJ2IjoiMSJ9.SVf1hFLKWPjFZM44nsYBTCc4-UApxNmn6E1nE1KNI197itlTdLuYiuvbpqHg_axNyg890u7TogpC8MwViJPYWTFQnruQiejzPwWUiy3ilzzdq9n2fbJHjDsyZXUzpTCN0zPamEP70NebfSMXP0P6BHDZ_dz9xv5TYR9UW2BTbLzcoYOtxqWoB9T5orMYmhbvMCaLXtv1CvF4pGPZY66I2_z4rQgj137IrFjjhN8pMI8._ER509e3bY-EUSMOrxpTxusdrrewmfYc3PG2W2bUDoU&dib_tag=se&keywords=laptop&qid=1731417433&sprefix=lapto%2Caps%2C299&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
elem = driver.find_element(By.CLASS_NAME, "puis-card-container")

print(elem.get_attribute("outerHTML"))
time.sleep(10)
driver.close()