from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from time import sleep
import requests, bs4

target_url = 'https://www.pfizerpro.co.uk'
options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=options, executable_path="/home/travis/build/harshilm/travis/chromedriver")
browser.get(target_url)
sleep(1)
try:
    pageName = browser.execute_script("return (s.pageName);")
    events = browser.execute_script("return (s.events);")
    print(pageName) #optional for console validation
    print(events) #optional for console validation
except WebDriverException:
    print("Exception on {}".format(url))
browser.quit()