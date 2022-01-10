





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\devops\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=s)


driver.get("https://www.researchgate.net/profile/Cvenkata-Siva-Prasad")
time.sleep(5)
driver.find_element(By.TAG_NAME, "input")