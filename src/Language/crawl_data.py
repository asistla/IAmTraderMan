from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
def getCsv(csvfile):
    with open(csvfile) as f:
        lines=f.readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].strip().split(',')
    return lines
    
def crawl():
#    options = webdriver.ChromeOptions()
#    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome Beta\\Application\\"
#    driver=webdriver.Chrome(chrome_options=options)
    driver=webdriver.Firefox()
    url="https://in.investing.com/indices/msci-world-stock-historical-data"
    driver.get(url)
    elem=driver.find_element(By.ID, value='widgetFieldDateRange')
    print elem
    return requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0'})