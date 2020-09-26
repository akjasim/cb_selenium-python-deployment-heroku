from selenium import webdriver
import time
from config import USERNAME, PASSWORD
import sys
import pyperclip
import os

try:
    repo_name = sys.argv[1]
except:
    print('Repo name is required.')
    sys.exit()

try:
    visibility = sys.argv[2]
except:
    visibility = 'public'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get(
    "CHROMEDRIVER_PATH"), options=chrome_options)


browser.get('https://github.com/login')

login_field = browser.find_element_by_name('login')
login_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_field.submit()

browser.get('https://github.com/new')

repo_field = browser.find_element_by_name('repository[name]')
repo_field.send_keys(repo_name)

visibility_field = browser.find_element_by_xpath(
    f'//input[@name="repository[visibility]"][@value="{visibility}"]')
visibility_field.click()

repo_field.submit()

try:
    copy_btn = browser.find_element_by_xpath(
        '//clipboard-copy[@for="empty-setup-push-repo-echo"]')
    copy_btn.click()

    print(pyperclip.paste())
except:
    print('Cannot create repository. (repo name should be unique)')
