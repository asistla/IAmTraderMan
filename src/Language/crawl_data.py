from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
def getCsv(csvfile):
    with open(csvfile) as f:
        lines=f.readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].strip().split(',')
    return lines
#[@class="popupCloseIcon largeBannerCloser"]
def crawl():
    driver=webdriver.Firefox()
    url="https://in.investing.com/indices/msci-world-stock-historical-data"
    driver.get(url)
    killPopup=driver.find_element(By.XPATH, value='//*[@id="PromoteSignUpPopUp"]//*[@class="popupCloseIcon largeBannerCloser"]')
    wait = WebDriverWait(killPopup, 30)
    wait.until(EC.visibility_of(killPopup))
    killPopup.click()
    print killPopup
    elem=driver.find_element(By.ID , value='widgetFieldDateRange')
    print elem
    return requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0'})