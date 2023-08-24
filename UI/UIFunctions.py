import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

def user_deposit(driver, selectors, deposit):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_login'])))
    customer_login_btn.click()
    time.sleep(2)

    hermione = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['hermione'])))
    hermione.click()
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

    # capture balance after deposit
    balance_after_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_after_deposit = int(balance_after_deposit.text)

    return balance_before_deposit, balance_after_deposit

# - כנס לבנק בתור משתמש תעשה הפקדה של 1000 שח ומשיכה של 250 תבדוק שמצב החשבון הוא 750

def user_balance(driver, selectors, deposit, withdraw):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_login'])))
    customer_login_btn.click()
    time.sleep(2)

    hermione = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['hermione'])))
    hermione.click()
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

    withdraw_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn1'])))
    withdraw_btn1.click()
    time.sleep(2)

    amount_tb2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb2'])))
    amount_tb2.send_keys(withdraw)
    time.sleep(2)

    withdraw_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn2'])))
    withdraw_btn2.click()
    time.sleep(2)

    # capture balance after deposit
    balance_after_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_after_deposit = int(balance_after_deposit.text)

    return balance_before_deposit, balance_after_deposit

# - כנס למערכת בהרשאות מנהל לחץ על כפתור משתמשים מחק אחד היוזרים לטעמך, כתוב טסט שבודק שהפעולה אכן בוצעה

def delete_customer(driver, selectors):
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to appear

    manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['manager_login_btn'])))
    manager_login_btn.click()
    time.sleep(2)

    customers_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_btn'])))
    customers_btn.click()
    time.sleep(2)

    # capture table before deletion
    customers_table_before = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_table']))).text

    delete_neville_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['delete_neville_btn'])))
    delete_neville_btn.click()
    time.sleep(2)

    # capture table after deletion
    customers_table_after = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customers_table']))).text

    return customers_table_before, customers_table_after

# - כנס למערכת בתור מנהל תעשה הוספה ללקוח חדש, תחזור למסך של המנהל ותבדוק שהלקוח שהכנסת אכן נמצא

def add_customer(driver, selectors):
    wait = WebDriverWait(driver, 3)  # Wait for up to 3 seconds for elements to appear

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
    first_name_tb.send_keys('Draco')
    time.sleep(2)

    last_name_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['last_name_tb'])))
    last_name_tb.send_keys('Malfoy')
    time.sleep(2)

    post_code_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['post_code_tb'])))
    post_code_tb.send_keys('E47832')
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
# המתאים url - כתוב קוד שנכנס למערכת בתור מנהל ותוסיף חשבון חדש תבדוק שאתה נמצא ב
# - תעשה בדיקת סאניטי למערכת
