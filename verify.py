from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests, bs4

target_url = 'https://www.pfizerpro.co.uk'
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

browser = webdriver.Chrome(executable_path="/home/travis/build/harshilm/travis/chromedriver", options=options)
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