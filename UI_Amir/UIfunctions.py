import re
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def get_driver(url):
    '''
    Initialize a WebDriver instance and navigate to the given URL.
    :param url: The URL to navigate to.
    :return: The WebDriver instance.
    '''
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        return driver
    except Exception as error:
        print(f"An error occurred in 'get_driver': {error}")

def user_withdrawl(driver,login_page,customer_page,account_page,customer_name,withdrawl,transaction_type):
    '''
    Perform a user withdrawal transaction.
    :param driver: The WebDriver instance.
    :param login_page: Selectors for login page elements.
    :param customer_page: Selectors for customer page elements.
    :param account_page: Selectors for account page elements.
    :param customer_name: Selector for customer's name.
    :param withdrawl: Amount to withdraw.
    :param transaction_type: Type of transaction.
    :return: A tuple containing the current time and the transaction table data.
    '''
    try:
        wait = WebDriverWait(driver, 10)
        customer_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['customer_login_btn'])))
        customer_login.click()
        customer_name_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
        customer_name_login.click()
        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_page['login_btn'])))
        login_btn.click()
        withdrawl_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['withdraw_btn'])))
        withdrawl_btn.click()
        amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['amount_tb'])))
        amount_tb.click()
        amount_tb.send_keys(withdrawl)
        amount_tb.send_keys(Keys.ENTER)
        current_time = datetime.now().strftime('%b %d, %Y %I:%M:%S %p')
        current_time = re.sub(r' 0(\d:)', r' \1', current_time)
        time.sleep(2)
        transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
        transaction_btn.click()
        time.sleep(2)
        date_time_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['date_time'])))
        date_time_btn.click()
        time.sleep(2)
        transaction_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
        time.sleep(1)
        current_time = current_time + ' ' + str(withdrawl) + transaction_type
        return current_time, transaction_table
    except Exception as error:
        print(f"An error occurred in 'user_withdrawl': {error}")

def check_account(driver,login_page,customer_page,account_page,customer_name):
    '''
    Check account transactions for different accounts.
    :param driver: The WebDriver instance.
    :param login_page: Selectors for login page elements.
    :param customer_page: Selectors for customer page elements.
    :param account_page: Selectors for account page elements.
    :param customer_name: Selector for customer's name.
    :return: Three lists containing transaction data for three different accounts.
    '''
    try:
        wait = WebDriverWait(driver, 10)
        customer_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['customer_login_btn'])))
        customer_login.click()
        customer_name_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
        customer_name_login.click()
        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_page['login_btn'])))
        login_btn.click()

        account_number1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['account_num_btn1'])))
        account_number1.click()
        transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
        transaction_btn.click()
        time.sleep(2)
        transaction_table1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
        time.sleep(1)
        back_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['back_btn'])))
        back_btn.click()
        time.sleep(1)

        account_number2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['account_num_btn2'])))
        account_number2.click()
        transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
        transaction_btn.click()
        time.sleep(2)
        transaction_table2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
        time.sleep(1)
        back_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['back_btn'])))
        back_btn.click()
        time.sleep(1)

        account_number3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['account_num_btn3'])))
        account_number3.click()
        transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
        transaction_btn.click()
        time.sleep(2)
        transaction_table3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
        time.sleep(1)
        lines1 = transaction_table1.split('\n')
        lines2 = transaction_table2.split('\n')
        lines3 = transaction_table3.split('\n')
        return lines1, lines2, lines3
    except Exception as error:
        print(f"An error occurred in 'check_account': {error}")

def check_transaction(driver, login_page, customer_page, account_page, customer_name, values):
    '''
    Check the number of transactions for a specific user.
    :param driver: The WebDriver instance.
    :param login_page: Selectors for login page elements.
    :param customer_page: Selectors for customer page elements.
    :param account_page: Selectors for account page elements.
    :param customer_name: Selector for customer's name.
    :param values: List of withdrawal values.
    :return: The count of successful transactions.
    '''
    try:
        wait = WebDriverWait(driver, 10)
        customer_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['customer_login_btn'])))
        customer_login.click()
        customer_name_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
        customer_name_login.click()
        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_page['login_btn'])))
        login_btn.click()
        time.sleep(2)

        withdrawl_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['withdraw_btn'])))
        withdrawl_btn.click()

        for i in range(len(values)):
            amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['amount_tb'])))
            amount_tb.send_keys(values[i])
            amount_tb.send_keys(Keys.ENTER)
            date = datetime.now().strftime('%b %d, %Y %I:%M:%S %p')
            date = re.sub(r' 0(\d:)', r' \1', date)
            values[i] = date + ' ' + str(values[i]) + ' Debit'

        time.sleep(2)
        transaction_btn = wait.until \
            (EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
        transaction_btn.click()
        time.sleep(2)
        date_time_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['date_time'])))
        date_time_btn.click()
        time.sleep(2)
        transaction_table_after = wait.until \
            (EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
        transaction_table_after = transaction_table_after.split('\n')

        count = 0
        for i in range(len(values)):
            for j in range(len(transaction_table_after)):
                if values[i] == transaction_table_after[j]:
                    count += 1
        return count
    except Exception as error:
        print(f"An error occurred in 'check_transaction': {error}")

def check_customers(driver,login_page,manager_page):
    '''
    Check the list of customers in the system.
    :param driver: The WebDriver instance.
    :param login_page: Selectors for login page elements.
    :param manager_page: Selectors for manager page elements.
    :return: A list of customer names.
    '''
    try:
        wait = WebDriverWait(driver, 10)
        manager_login_btn = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['manager_login_btn'])))
        manager_login_btn.click()
        customers_btn = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
        customers_btn.click()
        customers_table = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_table']))).text
        customers_table = customers_table.split('\n')
        return customers_table
    except Exception as error:
        print(f"An error occurred in 'check_customers': {error}")

def invalid_add_user(driver,login_page,manager_page,last_name,post_code):
    '''
    Attempt to add an invalid user and check the impact on the customer count.
    :param driver: The WebDriver instance.
    :param login_page: Selectors for login page elements.
    :param manager_page: Selectors for manager page elements.
    :param last_name: Last name of the user.
    :param post_code: Postal code of the user.
    :return: Two versions of the customer table before and after the invalid user addition attempt.
    '''
    try:
        wait = WebDriverWait(driver, 10)
        manager_login_btn = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['manager_login_btn'])))
        manager_login_btn.click()
        customers_btn = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
        customers_btn.click()

        customers_table_before = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_table']))).text
        add_customer_btn = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['add_customer_btn'])))
        add_customer_btn.click()

        last_name_tb = wait.until(EC.element_to_be_clickable
                                  ((By.CSS_SELECTOR, manager_page['last_name_tb'])))
        last_name_tb.send_keys(last_name)
        post_code_tb = wait.until(EC.element_to_be_clickable
                                  ((By.CSS_SELECTOR, manager_page['post_code_tb'])))
        post_code_tb.send_keys(post_code)
        post_code_tb.send_keys(Keys.ENTER)

        customers_btn = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_btn'])))
        customers_btn.click()
        customers_table_after = wait.until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, manager_page['customers_table']))).text
        return customers_table_after, customers_table_before
    except Exception as error:
        print(f"An error occurred in 'invalid_add_user': {error}")
