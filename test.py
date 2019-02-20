from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests, bs4
import pandas as pd
  
target_url = 'https://www.pfizerpro.co.uk' #starting url

# find all the links on the page
def findalllinks (url):

    #download the page
    print ('parsing...') #displaying text while parsing the page
    res = requests.get(url) #takes the string of the url to download
    res.raise_for_status() #will raise an exception if there is error downloading
    
    #retrieve all the links
    abhiSoup = bs4.BeautifulSoup(res.text,features="html.parser")
    linkel = abhiSoup.select('body a') #could be targeted to links within any element on page 
    
    #return a set of links
    numOpen = len(linkel)
    #print (numOpen) #optional for console validation
    linkel2 =[]  
    for i in range(numOpen):
        linkel2 = linkel2 + [(linkel[i].get('href'))]
    return linkel2 

# Visit the page
def pagehits(url):
    global HTML_string
    report = []
    #visit the page in a headless version of firefox
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #starting selenium controlled web browser
    #latest geckodriver is needed to run firefox with selenium
    browser = webdriver.Chrome(executable_path="/home/travis/build/harshilm/travis/chromedriver", options=options)
    browser.get(url)
    #give page time to load
    sleep(1)
    #log events and pagename
    #put the block in try/except
    try:
        pageName = browser.execute_script("return (s.pageName);")
        events = browser.execute_script("return (s.events);")
        report.append([pageName, events])
        
        print(pageName) #optional for console validation
        print(events) #optional for console validation
        print("-------------------")
        
        
    except WebDriverException:
        print("Exception on {}".format(url))
    browser.quit()

url_list = findalllinks(target_url)
# Iterate the links and collect data
for i in range(len(url_list)):
#for i in range(10,15):
    tag_link = str(url_list[i])
    if tag_link.startswith('/'):
        pagehits(target_url+tag_link)
    elif tag_link.startswith('http' or 'www'):
        pagehits(tag_link)
    else:
        continue
