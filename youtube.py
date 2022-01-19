from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from main import Youtube, db
from sqlalchemy.exc import IntegrityError

s = Service("C:\devops\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=s)


driver.get("https://www.youtube.com/c/ResearchPapersSupport/videos")
time.sleep(5)
data = driver.find_elements(By.ID, "video-title")[:5]

for d in data:
    text = d.text
    link = d.get_attribute('href')
    print(text, link)
    data_ = Youtube(name=text, link=link)
    db.session.add(data_)
    db.session.commit()


driver.close()
driver.quit()


