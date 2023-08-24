import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Bank_Selectors import selectors
'''
Programmers Notes: The time sleeps are not necessary needed for the code to work,
                   they are there to make it easier for the QA engineer
                   to see through the actions the code does.
'''
# - יש להיכנס למערכת עם אחד מהיוזרים הקיימים לעשות הפקדה של 250 ולראות שהמצב חשבון השתנה בהתאם

def get_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def user_deposit(driver, customer, deposit):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_selectors']['customer_login'])))
    customer_login_btn.click()
    time.sleep(2)

    account_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer)))
    account_btn.click()
    time.sleep(2)

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_btn'])))
    login_btn.click()
    time.sleep(2)

    # capture balance before deposit
    balance_before_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_before_deposit = int(balance_before_deposit.text)

    deposit_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn1'])))
    deposit_btn1.click()
    time.sleep(2)

    amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb'])))
    amount_tb.send_keys(deposit)
    time.sleep(2)

    deposit_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn2'])))
    deposit_btn2.click()
    # another possible option
    # press ENTER to submit the form
    # amount_tb.send_keys(Keys.ENTER)
    time.sleep(2)

    # capture balance after deposit
    balance_after_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_after_deposit = int(balance_after_deposit.text)

    return balance_before_deposit, balance_after_deposit

# - כנס לבנק בתור משתמש תעשה הפקדה של 1000 שח ומשיכה של 250 תבדוק שמצב החשבון הוא 750

def user_balance(driver, selectors, account, deposit, withdraw):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_login'])))
    customer_login_btn.click()
    time.sleep(2)

    account_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account)))
    account_btn.click()
    time.sleep(2)

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_btn'])))
    login_btn.click()
    time.sleep(2)

    # capture balance before deposit
    balance_before_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_before_deposit = int(balance_before_deposit.text)

    deposit_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn1'])))
    deposit_btn1.click()
    time.sleep(2)

    amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb'])))
    amount_tb.send_keys(deposit)
    time.sleep(2)

    deposit_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn2'])))
    deposit_btn2.click()
    time.sleep(2)

    # another possible option
    # press ENTER to submit the form
    # amount_tb.send_keys(Keys.ENTER)

    withdraw_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn1'])))
    withdraw_btn1.click()
    time.sleep(2)

    amount_tb2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb'])))
    amount_tb2.send_keys(withdraw)
    time.sleep(2)

    withdraw_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn2'])))
    withdraw_btn2.click()
    time.sleep(2)

    # another possible option
    # press ENTER to submit the form
    # amount_tb2.send_keys(Keys.ENTER)

    # capture balance after deposit
    balance_after_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_after_deposit = int(balance_after_deposit.text)

    return balance_before_deposit, balance_after_deposit

# - כנס למערכת בהרשאות מנהל לחץ על כפתור משתמשים מחק אחד היוזרים לטעמך, כתוב טסט שבודק שהפעולה אכן בוצעה

def delete_customer(driver, selectors, account_delete):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['manager_login_btn'])))
    manager_login_btn.click()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture table before deletion
    customers_table_before = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_table']))).text

    delete_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_delete)))
    delete_btn.click()
    time.sleep(2)

    # capture table after deletion
    customers_table_after = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_table']))).text

    return customers_table_before, customers_table_after

# - כנס למערכת בתור מנהל תעשה הוספה ללקוח חדש, תחזור למסך של המנהל ותבדוק שהלקוח שהכנסת אכן נמצא

def add_customer(driver, selectors, user_data):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['manager_login_btn'])))
    manager_login_btn.click()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture table before adding new customer
    customers_table_before = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_table']))).text

    add_customer_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['add_customer_btn'])))
    add_customer_btn.click()
    time.sleep(2)

    first_name_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['first_name_tb'])))
    first_name_tb.send_keys(user_data['first_name'])
    time.sleep(2)

    last_name_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['last_name_tb'])))
    last_name_tb.send_keys(user_data['last_name'])
    time.sleep(2)

    post_code_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['post_code_tb'])))
    post_code_tb.send_keys(user_data['post_code'])
    time.sleep(2)

    # add_customer_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['add_customer_btn2'])))
    # add_customer_btn2.click()
    # time.sleep(2)

    # another possible option
    # press ENTER to submit the form
    post_code_tb.send_keys(Keys.ENTER)
    time.sleep(2)

    # handle the alert
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture table after adding new customer
    customers_table_after = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_table']))).text

    return customers_table_before, customers_table_after

# - כתוב קוד שנכנס למערכת בתור מנהל ותוסיף חשבון חדש, תבדוק שאתה נמצא ב-url המתאים

def open_account(driver, selectors, account, currency):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['manager_login_btn'])))
    manager_login_btn.click()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # albus_num_data_old = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['albus_num_data']))).text

    open_account_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['open_account_btn'])))
    open_account_btn.click()
    time.sleep(2)

    customer_name_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account)))
    customer_name_btn.click()
    time.sleep(2)

    currency_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, currency)))
    currency_btn.click()
    time.sleep(2)

    # currency_text = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['pound_btn']))).text

    process_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['process_btn'])))
    process_btn.click()
    time.sleep(2)

    # handle the alert
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    time.sleep(2)

    return driver.current_url

    # customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_btn'])))
    # customers_btn.click()
    # time.sleep(2)
    #
    # albus_num_data_new = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['albus_num_data']))).text
    #
    # home_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['home_btn'])))
    # home_btn.click()
    # time.sleep(2)
    #
    # customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_login'])))
    # customer_login_btn.click()
    # time.sleep(2)
    #
    # albus = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['albus'])))
    # albus.click()
    # time.sleep(2)
    #
    # login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_btn'])))
    # login_btn.click()
    # time.sleep(2)
    #
    # account_number_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['account_number_btn'])))
    # account_number_btn.click()
    # time.sleep(2)

    # currency_type = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['currency_type']))).text

# - תעשה בדיקת סאניטי למערכת
