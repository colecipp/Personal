import requests
import urllib.request
import xlsxwriter
from bs4 import BeautifulSoup
import webbrowser
import time
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
from optparse import OptionParser

class SportsOracles():
    def names(self, website):
        result = requests.get(website) #website being scraped
        #print(result.status_code)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        name1 = []
        for h3_tag in soup.find_all('h3'):
            a_tag = h3_tag.find('a')
            try:
                if 'style' in a_tag.attrs:
                    temp = str(a_tag)
                    temp2 = temp.translate ({ord(c): "" for c in ',!@#%^&*()[]{};:./<>?\|`~=+"1234567890'}) #gets rid of characters
                    temp3 = temp2.replace('a classteam-name hrefhttpswwwspotraccomredirectplayer styleline-height px','') #gets rid of strings
                    temp3 = temp3[:-1] #gets rid of an extra character always attached to the end of the name
                    print(temp3)
                    name1.append(temp3)

            except:
                pass
        return name1

    def PFF(self, str):
        #allowing test run
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        driver = webdriver.Chrome('./chromedriver')
        url = 'https://www.google.com/'
        driver.get(url)
        #identify element
        element1 = driver.find_element(By.NAME, "q")
        search = "PFF " + str
        element1.send_keys(search)
        element1.send_keys(Keys.RETURN)
        #click PFF link
        link = driver.find_elements(By.CSS_SELECTOR, "a[ping^='/url?sa=t&source=web&rct=j&url=https://www.pff.com/nfl/playe'] > .DKV0Md.LC20lb.MBeuO")
        if not link:
            print("NOT FOUND **")

        else:
            element2 = driver.find_element(By.CSS_SELECTOR, "a[ping^='/url?sa=t&source=web&rct=j&url=https://www.pff.com/nfl/playe'] > .DKV0Md.LC20lb.MBeuO").click()
            driver.maximize_window()
            element3 = driver.find_element(By.TAG_NAME, "small").text
            element5 = element3.translate({ord(c): "" for c in ' ()'})
            print("Age: " + element5)
            #copy overall
            PFFOvrLink = driver.find_element(By.CSS_SELECTOR, ".kyber-grade-badge__info-text")
            if not PFFOvrLink:
                print("NO PFF SCORE")
            else:
                print("NO PFF SCORE")
                element4 = driver.find_element(By.CSS_SELECTOR, ".kyber-grade-badge__info-text").text
                print("PFF: " + element4)
            driver.close()
    def Insta(self, username):
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        driver = webdriver.Chrome('./chromedriver')
        url = 'https://www.instagram.com/' + username
        print(url)
        driver.get(url)
        element1 = driver.find_element(By.CLASS_NAME, '_ac2a _ac2b').click()
# xpath =       /*[@id="mount_0_0_+R"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/ul/li[3]/a/div
# //*[@id="mount_0_0_+R"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/ul/li[3]/a/div
def main():

        time1 = time.perf_counter()
        temp = "cole_cipp88"
        SportsOracles().Insta(temp)
        time2 = time.perf_counter()
        time3 = time2-time1
        print(time3, " sec")


if __name__ == "__main__":
    main()
