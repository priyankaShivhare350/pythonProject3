import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import pandas as pd

df=pd.read_csv("holiday.csv")
day=date.today()
for i in df["day"]:
    if i==str(day):
        print("yes")
        break
else:
    chrome_option=webdriver.ChromeOptions()
    chrome_option.add_argument("headless")
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://people.zoho.com/appzlogic/zp#home/dashboard")
    driver.find_element(By.LINK_TEXT,"SIGN IN").click()
    driver.find_element(By.ID,"login_id").send_keys("priyanka.shivhare@appzlogic.com")
    driver.find_element(By.ID,"nextbtn").click()
    time.sleep(20)
    driver.find_element(By.ID,"password").send_keys("Neon@#321")
    driver.find_element(By.ID,"nextbtn").click()
    time.sleep(20)
    driver.get("https://people.zoho.com/appzlogic/zp#home/dashboard")
    time.sleep(20)
    # driver.find_element(By.XPATH,"//*[@class='in chlodIng']").click()
    driver.find_element(By.ID,"ZPD_Top_Att_Stat").click()
    time.sleep(20)
    driver.get_screenshot_as_file("file1.png")
    driver.quit()



