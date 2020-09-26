from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

wait = WebDriverWait(browser, 10)

browser.get('https://github.com/login')

login_field = wait.until(
    EC.presence_of_element_located((By.NAME, "login"))
)
login_field.send_keys(USERNAME)

password_field = wait.until(
    EC.presence_of_element_located((By.NAME, "password"))
)

password_field.send_keys(PASSWORD)

login_field.submit()

browser.get('https://github.com/new')

repo_field = wait.until(EC.presence_of_element_located(
    (By.NAME, 'repository[name]')))
repo_field.send_keys(repo_name)

visibility_field = wait.until(EC.presence_of_element_located(
    (By.XPATH, f'//input[@name="repository[visibility]"][@value="{visibility}"]')))
visibility_field.click()

repo_field.submit()

try:
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//clipboard-copy[@for="empty-setup-push-repo-echo"]')))
    copy_btn.click()

    print(pyperclip.paste())
except:
    print('Cannot create repository. (repo name should be unique)')
