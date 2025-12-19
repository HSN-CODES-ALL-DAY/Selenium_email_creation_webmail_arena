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


def turn_off_emails(account, password):
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    url = 'https://steamcommunity.com/login/home/?goto='
    driver.get(url)

    WebDriverWait(driver, 25).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input._2GBWeup5cttgbTw8FM3tfx'))
    )

    elements = driver.find_elements(By.CSS_SELECTOR, value='input._2GBWeup5cttgbTw8FM3tfx')
    elements[0].send_keys(account) 
    elements[1].send_keys(password)
    time.sleep(2)

    sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button.DjSvCZoKKfoNSmarsEcTS')
    sign_in_button.click()
    time.sleep(6)
    if driver.current_url == 'https://steamcommunity.com/login/home/?goto=':
        print('login failed: ' + account)
        driver.delete_all_cookies()
        driver.refresh()
        driver.close()
        return False

    driver.get('https://store.steampowered.com/twofactor/manage/')
    email_authi_button = WebDriverWait(driver, 25).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input#email_authenticator_check'))
    )
    email_authi_button.click()
    time.sleep(3)

    driver.delete_all_cookies()
    driver.refresh()
    driver.close()
    
    return True

def updatetxt(account, filename):
    try:
        with open(filename, 'a') as f:
            f.write(account + '\n')
        print(f"Account {account} written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def remove_from_file(account_line, filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        with open(filename, 'w') as f:
            for line in lines:
                if line.strip() != account_line.strip():
                    f.write(line)
        print(f"Account removed from {filename}")
    except IOError as e:
        print(f"Error removing from file: {e}")

def process():
    ACC_FILE = 'account.txt'
    DONE_FILE = 'account_done.txt'
    try:
        with open(ACC_FILE, 'r') as f:
            all_accounts = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{ACC_FILE}' was not found.")
        return

    print(f"\nFound {len(all_accounts)} accounts to process.")
    print("-" * 40)

    for account_line in all_accounts:
        idpass = account_line.split(':')
        print(f"Processing: {idpass[0]}")
        
        success = turn_off_emails(idpass[0], idpass[1])
        
        if success:
            updatetxt(account_line, DONE_FILE)
            remove_from_file(account_line, ACC_FILE)
        else:
            print(f"Failed to process {idpass[0]}")


process()
