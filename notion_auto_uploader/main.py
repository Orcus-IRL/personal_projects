import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://www.notion.so/link continued ")
time.sleep(5)
email = 'can give my email'
driver.find_element(By.XPATH, '//*[@id="notion-email-input-2"]').send_keys(email, Keys.ENTER)

# enter the code
login_code = input("enter the login code: ")
driver.find_element(By.XPATH, '//*[@id="notion-password-input-1"]').send_keys(login_code, Keys.ENTER)

# settings and member
time.sleep(5)
settings_and_member = driver.find_element(By.XPATH,
                                          '//*[@id="notion-app"]/div/div[1]/div/nav/div/div/div/div[3]/div/div[2]/div[3]/div/div[1]')
print("Logged in successfully...")
time.sleep(1)
settings_and_member.click()

# settings and member -> settings
time.sleep(3)
settings = driver.find_element(By.XPATH,'//*[@id="notion-app"]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div/div/div[10]/div/div[1]')
time.sleep(1)
settings.click()

# settings and member -> settings -> export all content
time.sleep(3)
export_location = driver.find_element(By.XPATH,'//*[@id="notion-app"]/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[24]/div')
time.sleep(1)
export_location.click()
print("Got the export content...")

# settings and member -> settings -> export all content -> export
time.sleep(3)
export_button = driver.find_element(By.XPATH, '//*[@id="notion-app"]/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]')
time.sleep(1)
export_button.click()
print("Exporting...")

time.sleep(60)
print("content exported\nsession closed")
driver.close()
