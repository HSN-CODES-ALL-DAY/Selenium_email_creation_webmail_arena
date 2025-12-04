from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random
import string
import os
import hashlib


service = Service(r'C:\Users\hassa\OneDrive\Documents\Programming\chromedriver.exe')
options = Options()
options.add_argument('--log-level=3')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

def turn_off_emails(account, password):
    url = 'https://steamcommunity.com/login/home/?goto='
    driver.get(url)

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input._2GBWeup5cttgbTw8FM3tfx'))
    )


    elements = driver.find_elements(By.CSS_SELECTOR, value='input._2GBWeup5cttgbTw8FM3tfx')
    elements[0].send_keys('mikudagur8fq') 
    elements[1].send_keys('ff')
    time.sleep(2)



    sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button.DjSvCZoKKfoNSmarsEcTS')
    sign_in_button.click()
    time.sleep(10)
    if driver.current_url == 'https://steamcommunity.com/login/home/?goto=':
        print('login failed')



    driver.get('https://store.steampowered.com/twofactor/manage/')

    email_authi_button = driver.find_elements(By.CSS_SELECTOR, value='input#email_authenticator_check')
    email_authi_button.click()
    time.sleep(10)




    driver.delete_all_cookies()
    driver.refresh()
    time.sleep(500)

def process():
    ACC_FILE='account.txt'
    try:
        with open(ACC_FILE, 'r') as f:
            all_accounts = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{ACC_FILE}' was not found.")
        return

    print(f"\nFound {len(all_accounts)} accounts to process.")
    print("-" * 40)

    current_accounts = list(all_accounts) 
    for i in all_accounts:
        idpass=i.split(':')
        print(idpass[0])
        turn_off_emails(idpass[0],idpass[1])


def updatetxt(account, password,filename):
    file_name_done = 'account_done.txt'

process()
