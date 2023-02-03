These files are my journey into web-scraping. My main goal was to get as much data as I could for every NFL player; this meant going to various 
websites and pulling that data. I started with BeautifulSoup which did a lot of the heavy lifting but there were instances where I needed to use a 
search engine to get to the next stage. I was having trouble until I discovered Selenium, this allowed me to expand my project and I plan to continue 
this expansion by including data analytics and webpage capabilities. 

webscraper_bs44.py
IMPORTS:
requests
urllib.request
xlsxwriter
bs4
BeautifulSoup
webbrowser
- uses beautiful soup to grab data from https://www.spotrac.com/nfl/rankings/average/*team name*
- puts this data into an excel sheet "data.xlsx
- very basic, not fleshed out, improper formatting as this was just a test file

SeleniumTest.py
IMPORTS:
os
requests
urllib.request
xlsxwriter
bs4 
BeautifulSoup
webbrowser
time
re
selenium
webdriver
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
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import openpyxl

DATA POINTS:
Name, Position, Position's Average Salary, Age, Madden Rating, PFF Rating, Player Salary, PFR Rating
- uses beautiful soup to grab data from https://www.spotrac.com/nfl/rankings/average/*team name* & https://www.maddenratings.com/teams/*team name*
- uses the names and positions for the selenium webscraping
- the madden data set is the base to find salaries for players by comparing them to the spotrac data set and filling in the gaps
- The madden data set is used to google the selected player and find their Pro Football Focus rating/age by going to google.com, clicking the search box,
  typing in "PFF *Player Name* *Team Acronym*" clicking the link that matches a player profile on PFF, ex. https://www.pff.com/nfl/players/patrick-mahomes/11765,
  and extracting the PFF overall and age based on their CSS and tag respectively
- the madden data set is used to google the selected player and find their Por Football Reference approximated value  by going to google.com, clicking the search box, 
  typing in "PFR *Player Name* *Team Acronym*, and extracting their 2022 AV by sorting through a list of the CSS's that list the AV's (May find more efficient method)
- The madden data set is used to go through the set list of average salaries per position 
- currently each team is filtered through via their two webistes and their acronym
- an excel sheet is formatted and the data found was all put into lists to log into this excel sheet (should also log them into a Json file for future editing)

EFFICIENCY:
Team: 100% given the madden site is fully updated
Name: 100% given the madden site is fully updated
Pos: <100% given the madden site is fully updated
Madden Ovr: 100% given the madden site is fully updated
Sal: 83.32501%
Age: 85.47179%
PFF: 85.42187% hard to gauge b/c many players haven't played enough snaps to gain a PFF rating
PFR: <90.15990% could be wrong #



