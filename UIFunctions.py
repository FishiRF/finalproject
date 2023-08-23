import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# - יש להיכנס למערכת עם אחד מהיוזרים הקיימים לעשות הפקדה של 250 ולראות שהמצב חשבון השתנה בהתאם

def get_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def user_deposit(driver, selectors, deposit):
    wait = WebDriverWait(driver, 3)  # Wait for up to 3 seconds for elements to appear
    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_login'])))
    customer_login_btn.click()

    hermione = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['hermione'])))
    hermione.click()

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_btn'])))
    login_btn.click()

    # capture balance before deposit
    balance_before_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_before_deposit = int(balance_before_deposit.text)

    deposit_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn1'])))
    deposit_btn1.click()

    amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb'])))
    amount_tb.send_keys(deposit)

    deposit_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn2'])))
    deposit_btn2.click()

    # capture balance after deposit
    balance_after_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_after_deposit = int(balance_after_deposit.text)

    return balance_before_deposit, balance_after_deposit

# - כנס לבנק בתור משתמש תעשה הפקדה של 1000 שח ומשיכה של 250 תבדוק שמצב החשבון הוא 750

def user_balance(driver, selectors, deposit, withdraw):
    wait = WebDriverWait(driver, 3)  # Wait for up to 3 seconds for elements to appear

    customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_login'])))
    customer_login_btn.click()

    hermione = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['hermione'])))
    hermione.click()

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_btn'])))
    login_btn.click()

    # capture balance before deposit
    balance_before_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_before_deposit = int(balance_before_deposit.text)

    deposit_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn1'])))
    deposit_btn1.click()

    amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb'])))
    amount_tb.send_keys(deposit)
    time.sleep(3)

    deposit_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn2'])))
    deposit_btn2.click()

    withdraw_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn1'])))
    withdraw_btn1.click()
    time.sleep(3)

    amount_tb2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb2'])))
    amount_tb2.send_keys(withdraw)
    time.sleep(3)

    withdraw_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn2'])))
    withdraw_btn2.click()

    # capture balance after deposit
    balance_after_deposit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
    balance_after_deposit = int(balance_after_deposit.text)

    return balance_before_deposit, balance_after_deposit

# url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
# driver = webdriver.Chrome()
# driver.get(url)
# selectors = {
#             'customer_login': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
#             'hermione': '#userSelect > option:nth-child(2)',
#             'login_btn': 'body > div > div > div.ng-scope > div > form > button',
#             'deposit_btn1': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
#             'amount_tb': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
#             'deposit_btn2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
#             'withdraw_btn1': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
#             'amount_tb2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
#             'withdraw_btn2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
#             'balance': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)'
#             }
#
# wait = WebDriverWait(driver, 3)  # Wait for up to 3 seconds for elements to appear
#
# customer_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_login'])))
# customer_login_btn.click()
#
# hermione = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['hermione'])))
# hermione.click()
#
# login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_btn'])))
# login_btn.click()
#
# deposit_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn1'])))
# deposit_btn1.click()
#
# amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb'])))
# amount_tb.send_keys(1000)
# time.sleep(3)
#
# deposit_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['deposit_btn2'])))
# deposit_btn2.click()
#
# withdraw_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn1'])))
# withdraw_btn1.click()
# time.sleep(3)
#
# amount_tb2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['amount_tb2'])))
# amount_tb2.send_keys(250)
# time.sleep(3)
#
# withdraw_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['withdraw_btn2'])))
# withdraw_btn2.click()
#
# balance = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['balance'])))
# print(int(balance.text))
# driver.quit()

# - כנס למערכת בהרשאות מנהל לחץ על כפתור משתמשים מחק אחד היוזרים לטעמך, כתוב טסט שבודק שהפעולה אכן בוצעה

# - כנס למערכת בתור מנהל תעשה הוספה ללקוח חדש, תחזור למסך של המנהל ותבדוק שהלקוח שהכנסת אכן נמצא

# המתאים url - כתוב קוד שנכנס למערכת בתור מנהל ותוסיף חשבון חדש תבדוק שאתה נמצא ב
# - תעשה בדיקת סאניטי למערכת
