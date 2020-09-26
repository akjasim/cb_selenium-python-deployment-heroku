from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def scrape_top_news():

    browser = webdriver.Chrome(
        executable_path="/Users/akjasim/chromedriver/chromedriver")

    wait = WebDriverWait(browser, 10)
    browser.get('https://news.ycombinator.com/')
    element_list = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".title > a"))
    )
    for element in element_list:
        try:
            title, url = element.text, element.get_attribute('href')
            print("Title:", title, "\nURL:", url, end="\n\n")
        except Exception as e:
            print(e)
    time.sleep(2)
    browser.quit()


if __name__ == '__main__':
    scrape_top_news()
