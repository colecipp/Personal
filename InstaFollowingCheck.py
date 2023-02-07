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
    def Insta(self, username, password):
        PATH = r"C:\download\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get("https://www.instagram.com/")

        #login
        time.sleep(2)
        try:
            username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        except:
            time.sleep(3)
            try:
                username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
            except:
                print("COMPUTER TOO SLOW TRY AGAIN")

            print("USERNAME FAILED")
        password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        username.clear()
        password.clear()
        username.send_keys("cole_cipp88")
        password.send_keys("BellportG1a2M3eFootballB4r5e6a7k8e9r88")
        login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        #save your login info?
        time.sleep(3)
        try:
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #turn on notif
        time.sleep(3)
        try:
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #searchbox
        time.sleep(2)

        try:
            profile = driver.find_element(By.LINK_TEXT,'cole_cipp88').click()
            # for element in profile:
            #      print(element.text)
        except:
            print("ERROR1")

        time.sleep(3)
        get_url = driver.current_url
        if get_url == "https://www.instagram.com/cole_cipp88/":
            try:
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                print("SUCCESS")
                # for element in profile:
                #      print(element.text)
            except:
                time.sleep(5)
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                                                       #/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']/span/span[.='637']
                                                       #/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']
                get_url1 = driver.current_url
                if get_url1 == "https://www.instagram.com/cole_cipp88/following/":
                    print('SUCCESS')
        else:
            print("ERROR2")

        time.sleep(3)
        # people = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div")
        #:not(._aacl _aaco _aacu _aacy _aada)
        people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")
                                                       #._aano ._aba8._abcm:nth-of-type(2) ._ab97._ab9f
                                                #/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div/div[2]/div[2]/div[1]//a[@role='link']//div[.='ryan.baumann']
                                                #/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div/div[14]/div[2]/div[1]//a[@role='link']//div[.='sabrinacarlaaa']
        FollowingList = []
        for element in people:
            if "ollowing" in element.text:
                pass
            else:
                # print(element.text)
                FollowingList.append(element.text)


        # scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        link3 = "/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div"
        instruct = "document.querySelector(" + link3 + ").scrollBy(0,1000)"
        xpath_element = " /html/body/div[2]//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']"
        following = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']//span[@class='_ac2a']/span")
                                                  #/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']//span[@title='870']/span[.='870']
        followers = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']//span[@class='_ac2a']/span")
        # print("Followers: ", followers.text)
        FollowerNum = followers.text
        FollowingNum = following.text
        FollowerScroll = ((int(FollowerNum)/12)+1)*3
        FollowingScroll = ((int(FollowingNum)/12)+1)*3
        # print(FollowerScroll, " ", FollowingScroll, "***")
        # print("Following: ", following.text)
        fBody = driver.find_element(By.XPATH, xpath_element)
        scroll = 0
        while scroll < FollowingScroll:  # this will scroll 3 times
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',fBody)
            scroll += 1
              # add appropriate wait here, of course. 1-2 seconds each
            time.sleep(2)

        # try:
        #     # scrolldown = driver.execute_script(instruct)
        #     # scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        #     scrolldown = driver.execute_script("document.querySelector(@class='x1uhb9sk').scrollBy(0,1000)")
        #     time.sleep(3)
        #     print("SUCCESS")
        try:
            people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")
                                                           #._aano ._aba8._abcm:nth-of-type(1) ._ab97._ab9f
            # print("Bruh")
            # var dict = subCategoriesList.ToDictionary(s => s.subCategoryID, s => s);
            # var matches = userInsideCategoriesList.Where(l => dict.ContainsKey(l.iDfromSubCategories));
            for element in people:
                # print("Bruh2")
                if "ollowing" in element.text:
                    # print("Bruh3")
                    pass

                elif element.text in FollowingList:
                    pass
                else:
                    # print(element.text)
                    FollowingList.append(element.text)
            # print("Bruh4")
        except:
            print("ERROR5")
        # except:
        #     print("ERROR4")
        # match=False
        # while(match==False):
        #     last_count = scrolldown
        #     time.sleep(3)
        #     scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        #     if last_count==scrolldown:
        #         match=True
        print(FollowingList)
        print(len(FollowingList))
        driver.close()
        return FollowingList
    def Insta2(self, username, password):
        PATH = r"C:\download\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get("https://www.instagram.com/")

        #login
        time.sleep(2)
        try:
            username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        except:
            time.sleep(3)
            try:
                username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
            except:
                print("COMPUTER TOO SLOW TRY AGAIN")

            print("USERNAME FAILED")
        password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        username.clear()
        password.clear()
        username.send_keys("cole_cipp88")
        password.send_keys("BellportG1a2M3eFootballB4r5e6a7k8e9r88")
        login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        #save your login info?
        time.sleep(3)
        try:
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #turn on notif
        time.sleep(3)
        try:
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #searchbox
        time.sleep(2)

        try:
            profile = driver.find_element(By.LINK_TEXT,'cole_cipp88').click()
            # for element in profile:
            #      print(element.text)
        except:
            print("ERROR1")

        time.sleep(3)
        get_url = driver.current_url
        if get_url == "https://www.instagram.com/cole_cipp88/":
            try:
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                print("SUCCESS")
                # for element in profile:
                #      print(element.text)
            except:
                time.sleep(5)
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                                                       #/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']/span/span[.='637']
                                                       #/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']
                get_url1 = driver.current_url
                if get_url1 == "https://www.instagram.com/cole_cipp88/followers/":
                    print('SUCCESS')
                else:
                    print("ERROR2")

        time.sleep(3)
            # people = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div")
            #:not(._aacl _aaco _aacu _aacy _aada)
        people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")
                                                       #._aano ._aba8._abcm:nth-of-type(2) ._ab97._ab9f
                                                #/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div/div[2]/div[2]/div[1]//a[@role='link']//div[.='ryan.baumann']
                                                #/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div/div[14]/div[2]/div[1]//a[@role='link']//div[.='sabrinacarlaaa']
        FollowerList = []
        for element in people:
            if "remove" in element.text:
                pass
            else:
                print(element.text)
                fixed1 = element.text
                fixed2 = fixed1.replace("follow", "")
                FollowerList.append(fixed2)


        # scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        link3 = "/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div"
        instruct = "document.querySelector(" + link3 + ").scrollBy(0,1000)"
        xpath_element = " /html/body/div[2]//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']"
        # following = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']//span[@class='_ac2a']/span")
        #                                           #/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']//span[@title='870']/span[.='870']
        followers = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']//span[@class='_ac2a']/span")
        # print("Followers: ", followers.text)
        FollowerNum = followers.text
        # FollowingNum = following.text
        FollowerScroll = ((int(FollowerNum)/12)+1)*3
        # FollowingScroll = ((int(FollowingNum)/12)+1)*3
        # print(FollowerScroll, " ", FollowingScroll, "***")
        # print("Following: ", following.text)
        fBody = driver.find_element(By.XPATH, xpath_element)
        scroll = 0
        while scroll < FollowerScroll:  # this will scroll 3 times
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',fBody)
            scroll += 1
              # add appropriate wait here, of course. 1-2 seconds each
            time.sleep(2)

        try:
            people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")
                                                           #._aano ._aba8._abcm:nth-of-type(1) ._ab97._ab9f
            # print("Bruh")
            # var dict = subCategoriesList.ToDictionary(s => s.subCategoryID, s => s);
            # var matches = userInsideCategoriesList.Where(l => dict.ContainsKey(l.iDfromSubCategories));
            for element in people:
                # print("Bruh2")
                if "remove" in element.text:
                    # print("Bruh3")
                    pass

                elif element.text in FollowerList:
                    pass
                else:
                    print(element.text)
                    fixed1 = element.text
                    fixed2 = fixed1.replace("follow", "")
                    FollowerList.append(fixed2)
            # print("Bruh4")
        except:
            print("ERROR5")

        print(FollowerList)
        print(len(FollowerList))
        return FollowerList
    def InstaCheck(self, FollowingList, FollowerList):
        NotFollowingYou = []
        for element in FollowingList:
            if element in FollowerList:
                pass
            elif "\nVerified" in element:
                pass
            else:
                NotFollowingYou.append(element)
        print(NotFollowingYou)
        return NotFollowingYou
    def BSInsta(self, username):
        website = 'https://www.instagram.com/' + username
        result = requests.get(website)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        name1 = []
        for ul_tag in soup.find_all('ul'):
            temp1 = str(ul_tag)
            print(temp1)
            li_tag = ul_tag.find('li')
            temp2 = str(li_tag)
            print(temp2)
            try:
                if 'href' in li_tag.attrs:
                    temp3 = str(li_tag)
                    # start = temp.find('>') + 1
                    # end = temp.find('<', start)
                    # name = temp[start:end]
                    # if name.find(" "):
                    name1.append(temp3)
            except:
                print("FAILURE")
                pass
        print(name1)
        return name1

def main():

        time1 = time.perf_counter()
        temp = "cole_cipp88"
        temp2 = "BellportG1a2M3eFootballB4r5e6a7k8e9r88"
        Following = SportsOracles().Insta(temp, temp2)
        time2 = time.perf_counter()
        time3 = time2-time1
        print(time3, " sec")
        time4 = time.perf_counter()
        Followers = SportsOracles().Insta2(temp, temp2)
        time5 = time.perf_counter()
        time6 = time2-time1
        print(time6, " sec")
        Rude = SportsOracles().InstaCheck(Following, Followers)




if __name__ == "__main__":
    main()
