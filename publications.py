from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from main import BlogPost, db
from sqlalchemy.exc import IntegrityError

s = Service("C:\devops\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=s)


driver.get("https://www.researchgate.net/profile/Cvenkata-Siva-Prasad")
time.sleep(5)
data = driver.find_elements(By.XPATH, '//div[@itemprop="headline"]')


for d in data:
    text = d.text
    link = driver.find_element(By.XPATH, f'//a[text()="{d.text}"]').get_attribute("href")
    try:
        data = BlogPost(name=text, link=link)
        db.session.add(data)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

driver.close()
driver.quit()