import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
'''
Programmers Notes: The time sleeps are not necessary needed for the code to work,
                   they are there to make it easier for the QA engineer
                   to see through the actions the code does.
'''

def get_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def user_deposit(driver, login_page, customer_page, account_page, customer_name, deposit):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['customer_login_btn'])))
    customer_login_btn.click()
    time.sleep(2)

    customer_name_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
    customer_name_btn.click()
    time.sleep(2)

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_page['login_btn'])))
    login_btn.click()
    time.sleep(2)

    # capture balance before deposit
    balance = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['balance_number'])))
    balance = int(balance.text)

    deposit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['deposit_btn'])))
    deposit_btn.click()
    time.sleep(2)

    amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['amount_tb'])))
    amount_tb.send_keys(deposit)
    time.sleep(2)

    # press ENTER to submit the form
    amount_tb.send_keys(Keys.ENTER)
    time.sleep(2)

    # capture balance after deposit
    updated_balance = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['balance_number'])))
    updated_balance = int(updated_balance.text)

    return balance, updated_balance

def user_balance(driver, login_page, customer_page, account_page, customer_name, deposit, withdraw):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['customer_login_btn'])))
    customer_login_btn.click()
    time.sleep(2)

    customer_name_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
    customer_name_btn.click()
    time.sleep(2)

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_page['login_btn'])))
    login_btn.click()
    time.sleep(2)

    # capture balance before deposit
    balance = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['balance_number'])))
    balance = int(balance.text)

    deposit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['deposit_btn'])))
    deposit_btn.click()
    time.sleep(2)

    amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['amount_tb'])))
    amount_tb.send_keys(deposit)
    time.sleep(2)

    # press ENTER to submit the form
    amount_tb.send_keys(Keys.ENTER)
    time.sleep(2)

    withdraw_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['withdraw_btn'])))
    withdraw_btn.click()
    time.sleep(2)

    amount_tb2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['amount_tb'])))
    amount_tb2.send_keys(withdraw)
    time.sleep(2)

    # press ENTER to submit the form
    amount_tb2.send_keys(Keys.ENTER)
    time.sleep(2)

    # capture balance after deposit
    updated_balance = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['balance_number'])))
    updated_balance = int(updated_balance.text)

    return balance, updated_balance

def delete_customer(driver, login_page, manager_page, customer_delete, data):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['manager_login_btn'])))
    manager_login_btn.click()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture table and customer data before deletion
    customers_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_table']))).text
    customer_data = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, data))).text

    delete_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_delete)))
    delete_btn.click()
    time.sleep(2)

    # capture table after deletion
    updated_customers_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_table']))).text

    return customers_table, updated_customers_table, customer_data

def add_customer(driver, login_page, manager_page, user_data):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['manager_login_btn'])))
    manager_login_btn.click()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture table before adding new customer
    customers_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_table']))).text

    add_customer_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['add_customer_btn'])))
    add_customer_btn.click()
    time.sleep(2)

    first_name_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['first_name_tb'])))
    first_name_tb.send_keys(user_data['first_name'])
    time.sleep(2)

    last_name_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['last_name_tb'])))
    last_name_tb.send_keys(user_data['last_name'])
    time.sleep(2)

    post_code_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['post_code_tb'])))
    post_code_tb.send_keys(user_data['post_code'])
    time.sleep(2)

    # press ENTER to submit the form
    post_code_tb.send_keys(Keys.ENTER)
    time.sleep(2)

    # handle the alert
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture table after adding new customer
    updated_customers_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_table']))).text

    return customers_table, updated_customers_table

def open_account(driver, login_page, manager_page, customer_name, currency, data):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['manager_login_btn'])))
    manager_login_btn.click()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture customer data before opening an account
    customer_data = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, data))).text

    open_account_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['open_account_btn'])))
    open_account_btn.click()
    time.sleep(2)

    open_account_url = driver.current_url

    customer_name_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
    customer_name_btn.click()
    time.sleep(2)

    currency_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, currency)))
    currency_btn.click()
    time.sleep(2)

    process_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['process_btn'])))
    process_btn.click()
    time.sleep(2)

    # handle the alert
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    time.sleep(2)

    current_url = driver.current_url

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture customer data after opening an account
    updated_customer_data = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, data))).text

    return current_url, open_account_url, customer_data, updated_customer_data

def sanity_test(driver):
    current_url = driver.current_url
    res = requests.get(current_url)
    return res.status_code