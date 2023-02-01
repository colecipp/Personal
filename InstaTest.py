import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException
import time, urllib.request
import requests

PATH = r"C:\download\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

#login
time.sleep(5)
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys("cole_cipp88")
password.send_keys("BellportG1a2M3eFootballB4r5e6a7k8e9r88")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#save your login info?
time.sleep(5)
notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(5)
notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

#searchbox
time.sleep(5)
profile = driver.find_element(By.CLASS_NAME, 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd')
if not link:
    element1 = SportsOracles().SpotracBackup1(str, team)
else:
    element1 = link.text
