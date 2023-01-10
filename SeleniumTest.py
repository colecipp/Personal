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

        # #copy age
        # element3 = driver.find_element(By.TAG_NAME, "small").text
        # element5 = element3.translate({ord(c): "" for c in ' ()'})
        # print("Age: " + element5)
        # #copy overall
        # if driver.find_element(By.CSS_SELECTOR, ".kyber-grade-badge__info-text") != 0:

        #     element4 = driver.find_element(By.CSS_SELECTOR, ".kyber-grade-badge__info-text").text
        #     print("PFF: " + element4)
        # else:
        #     Print("NO PFF SCORE")
        # driver.close()
        # return element4, element5

    def PFR():
        #allowing test run
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        driver = webdriver.Chrome('./chromedriver')
        url = 'https://www.google.com/'
        driver.get(url)
        #identify element
        element1 = driver.find_element(By.NAME, "q")
        search = "PFF" + " Joey Bosa"
        element1.send_keys(search)
        element1.send_keys(Keys.RETURN)
        element2 = driver.find_element(By.CSS_SELECTOR, "div#rso > div:nth-of-type(1) > .MjjYud > .Ww4FFb.g.tF2Cxc.vt6azd > .BToiNc.UK95Uc.kvH3mc a[ping^='/url?sa=t&source=web&rct=j&url=https://www.pff.com/nfl/playe'] > .DKV0Md.LC20lb.MBeuO").click()
        print("Test Ran")

    # def Salary(website):
    #     result = requests.get(website) #website being scraped
    #     #print(result.status_code)
    #     src = result.content
    #     soup = BeautifulSoup(src, 'lxml')
    #     salaries = [] #array of salaries which is what is being searched below

    #     for td_tag in soup.find_all('td'): # I've seen simpler versions of this but I couldn't get them to work for the data I needed
    #         span_tag = td_tag.find('span')
    #         try:
    #             if 'class' in span_tag.attrs:
    #                 temp = str(span_tag)
    #                 temp2 = temp.translate ({ord(c): "" for c in ' !@#%^&*()[]{};:./<>?\|`~-=_+classeminfotitlespanvoidVFrhRLT"'}) #getting rid of all the unnecessary characters
    #                 salaries.append(temp2)

    #         except:
    #             pass
    #     return salaries
    # def Positions(website):
    #     result = requests.get(website) #website being scraped
    #     #print(result.status_code)
    #     src = result.content
    #     soup = BeautifulSoup(src, 'lxml')
    #     tmp = str(salaries) #unused
    #     length = len(names)
    #     positions = []
    #     positionsSal = [] #average salaray for each specified position, this allows me to come up with a deserved salary for the player versus their actual salary
    #     td = soup.select('td')
    #     for name, value in zip(td, td[1:]): #checking the position stated on the website and converting it into the positions I have for their salaries and for the chart
    #         try:
    #             temp = str(name.text)

    #             if " QB " in temp:
    #                 positions.append("QB")
    #                 positionsSal.append("$5,740,484")
    #             elif " RB " in temp:
    #                 positions.append("HB")
    #                 positionsSal.append("$1,771,731")
    #             elif " FB " in temp:
    #                 positions.append("FB")
    #                 positionsSal.append("$1,266,088")
    #             elif " WR " in temp:
    #                 positions.append("WR")
    #                 positionsSal.append("$2,390,355")
    #             elif " TE " in temp:
    #                 positions.append("TE")
    #                 positionsSal.append("$1,983,261")
    #             elif " LT " in temp:
    #                 positions.append("OT")
    #                 positionsSal.append("$3,536,357")
    #             elif " RT " in temp:
    #                 positions.append("OT")
    #                 positionsSal.append("$3,536,357")
    #             elif " G " in temp:
    #                 positions.append("OG")
    #                 positionsSal.append("$2,451,945")
    #             elif " C " in temp:
    #                 positions.append("C")
    #                 positionsSal.append("$2,558,048")
    #             elif " DE " in temp:
    #                 positions.append("DE")
    #                 positionsSal.append("$3,198,393")
    #             elif " DT " in temp:
    #                 positions.append("DT")
    #                 positionsSal.append("$2,991,040")
    #             elif " OLB " in temp:
    #                 positions.append("OLB")
    #                 positionsSal.append("$2,782,424")
    #             elif " ILB " in temp:
    #                 positions.append("MLB")
    #                 positionsSal.append("$3,350,875")
    #             elif " LB " in temp:
    #                 positions.append("OLB")
    #                 positionsSal.append("$2,782,424")
    #             elif " CB " in temp:
    #                 positions.append("CB")
    #                 positionsSal.append("$2,206,489")
    #             elif " FS " in temp:
    #                 positions.append("FS")
    #                 positionsSal.append("$3,548,345")
    #             elif " SS " in temp:
    #                 positions.append("SS")
    #                 positionsSal.append("$3,237,867")
    #             elif " S " in temp:
    #                 positions.append("FS")
    #                 positionsSal.append("$3,548,345")
    #             elif " T " in temp:
    #                 positions.append("OT")
    #                 positionsSal.append("$3,536,357")
    #             elif " K " in temp:
    #                 positions.append("K")
    #                 positionsSal.append("$1,933,002")
    #             elif " P " in temp:
    #                 positions.append("P")
    #                 positionsSal.append("$1,517,049")
    #             elif " LS " in temp:
    #                 positions.append("LS")
    #                 positionsSal.append("$949,060")
    #             # else:
    #             #     positions.append("")
    #         except:
    #             pass
    #     return positions, positionsSal, length


    # def ExcelSheet(length, positions, names, salaries, positionsSal):
    #     workbook = xlsxwriter.Workbook('data.xlsx') #the rest is making an excel sheet
    #     worksheet = workbook.add_worksheet()

    #     # Widen the first column to make the text clearer.
    #     worksheet.set_column('A:A', 12.5)
    #     worksheet.set_column('B:B', 7.5)
    #     worksheet.set_column('C:C', 19.5)
    #     worksheet.set_column('D:D', 13.5)
    #     worksheet.set_column('E:E', 7.5)
    #     worksheet.set_column('F:F', 7.5)
    #     worksheet.set_column('G:G', 7.5)
    #     worksheet.set_column('H:H', 6.5)
    #     worksheet.set_column('I:I', 7.5)
    #     worksheet.set_column('J:J', 8.5)
    #     worksheet.set_column('K:K', 9.5)
    #     worksheet.set_column('L:L', 15.5)
    #     worksheet.set_column('M:M', 21.5)
    #     worksheet.set_column('N:N', 18.5)
    #     worksheet.set_column('O:O', 16.5)
    #     worksheet.set_column('P:P', 8.5)
    #     worksheet.set_column('Q:Q', 11.5)
    #     worksheet.set_column('R:R', 10.5)
    #     worksheet.set_column('S:S', 8.5)
    #     worksheet.set_column('T:T', 12.5)
    #     worksheet.set_column('U:U', 12.5)
    #     # Add a bold format to use to highlight cells.
    #     format = workbook.add_format({'align': 'center'})
    #     format.set_font_name("Times New Roman")
    #     format.set_font_size(12)
    #     format.set_align('center')
    #     format.set_align('vcenter')

    #     worksheet.write('A1', 'Team', format)
    #     worksheet.write('B1', 'Position', format)
    #     worksheet.write('C1', 'Player', format)
    #     worksheet.write('D1', 'Average Salary', format)
    #     worksheet.write('E1', 'Age', format)
    #     worksheet.write('F1', 'Madden', format)
    #     worksheet.write('G1', 'PFF', format)
    #     worksheet.write('H1', 'PFR', format)
    #     worksheet.write('I1', 'Lineups', format)
    #     worksheet.write('J1', 'Injury Prj', format)
    #     worksheet.write('K1', 'Overall', format)
    #     worksheet.write('L1', 'Ovr (adj. Age/Inj)', format)
    #     worksheet.write('M1', 'Average Position Salary', format)
    #     worksheet.write('N1', 'Deserved Salary', format)
    #     worksheet.write('O1', 'Salary Difference', format)
    #     worksheet.write('P1', '', format)
    #     worksheet.write('Q1', 'Yrs w/ Team', format)
    #     worksheet.write('R1', 'Acquired', format)
    #     worksheet.write('S1', 'Drafted', format)
    #     worksheet.write('T1', 'Draft Class', format)
    #     worksheet.write('U1', 'Position Rank', format)
    #     # Write some numbers, with row/column notation.
    #     for i in range(length):
    #         j = str(i+2)
    #         worksheet.write(i+1, 0, "Patriots", format)
    #         worksheet.write(i+1, 1, positions[i], format)
    #         worksheet.write(i+1, 2, names[i], format)
    #         worksheet.write(i+1, 3, salaries[i], format)
    #         worksheet.write(i+1, 10, "=(F" + j + "*0.3611)+(G" + j + "*1.1*0.3611)+(H" + j + "*5.2*0.0666)+(I"  + j + "*0.2111)", format) #some formulas I came up with for the values that I want
    #         worksheet.write(i+1, 11, "=(K"  + j + ")*((100+(29-E"  + j + "))/100)-(J" + j + "*0.9)", format)
    #         worksheet.write(i+1, 12, positionsSal[i], format)
    #         worksheet.write(i+1, 13, "=(M"  + j + "*((L"  + j + "-63)/5.45))+M" + j, format)
    #         worksheet.write(i+1, 14, "=(N" + j + "-D" + j + ")", format)
    #         worksheet.write(i+1, 15, '=IF(O' + j + '<(-3000000), "Overpaid", "")', format)

    #     workbook.close()
def main():
    team1 = "https://www.spotrac.com/nfl/rankings/average/arizona-cardinals/"
    # player1 = "Joey Bosa"
    # PFF(player1)
    for temp in SportsOracles().names(team1):
        # PFFRatings = []
        # PlayerAge = []
        print(temp)
        time1 = time.perf_counter()
        SportsOracles().PFF(temp)
        time2 = time.perf_counter()
        time3 = time2-time1
        print(time3, " sec")


if __name__ == "__main__":
    main()

# def test2():
#     return 'abc', 100, [0, 1, 2]

# a, b, c = test2() 
