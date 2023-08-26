import pytest
from UIFunctions import *
from Bank_Selectors import *
import traceback
import os

class TestUI:
    @pytest.fixture
    def url(self):
        '''
        Returns the URL of the test application.
        '''
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def take_screenshot(self, driver, test_name):
        '''
        Takes a screenshot of the current state of the browser window and saves it to a file.
        :param driver: The WebDriver instance.
        :param test_name: The name of the test.
        '''
        try:
            # Create a directory to store screenshots if it doesn't exist
            screenshot_dir = 'UI_Test_Errors'
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            # Define the path for the screenshot using the test name
            screenshot_path = os.path.join(screenshot_dir, f'{test_name}.png')
            # Save the screenshot and print the path
            driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved: {screenshot_path}')
        except Exception as error:
            print(f'Error occurred while capturing a screenshot: {error}')

    def test1_user_deposit(self, url):
        '''
        Test case to simulate user deposit functionality.
       :param url: The URL of the application.
       '''
        # Initialize the driver outside the try block
        # to ensure it's accessible in the finally block
        driver = None
        try:
            driver = get_driver(url)
            balance, updated_balance = user_deposit\
            (driver, selectors['login_page'], selectors['customer_page'],
             selectors['account_page'], selectors['customer_page']['hermione'], 250)
            # Check if balance increased by 250
            assert updated_balance == balance + 250,\
                   'Balance did not increase by the expected amount.'
        except Exception as error:  # can use AssertionError here
            # If assertion fails
            self.take_screenshot(driver, 'test1_error')  # capture a screenshot
            traceback.print_exc()  # print the error traceback
            raise  # re-raise the exception
        finally:
            # Quit the driver regardless of whether an exception was raised or not
            if driver:
                driver.quit()

    def test2_user_balance(self, url):
        '''
        Test case to simulate user balance functionality.
        :param url: The URL of the application.
        '''
        # Initialize the driver outside the try block
        # to ensure it's accessible in the finally block
        driver = None
        try:
            driver = get_driver(url)
            balance, updated_balance = user_balance\
            (driver, selectors['login_page'], selectors['customer_page'],
             selectors['account_page'], selectors['customer_page']['ron'], 1000, 250)
            # Check if balance increased by 750
            assert updated_balance == balance + 750,\
                   'Balance did not increase by the expected amount.'
        except Exception as error:  # can use AssertionError here
            # If assertion fails
            self.take_screenshot(driver, 'test2_error')  # capture a screenshot
            traceback.print_exc()  # print the error traceback
            raise  # Re-raises the exception to ensure proper reporting
        finally:
            # Quit the driver regardless of whether an exception was raised or not
            if driver:
                driver.quit()

    def test3_delete_customer(self, url):
        '''
        Test case to simulate deleting a customer.
        :param url: The URL of the application.
        '''
        # Initialize the driver outside the try block
        # to ensure it's accessible in the finally block
        driver = None
        try:
            driver = get_driver(url)
            customers_table, updated_customers_table, customer_data = delete_customer\
            (driver, selectors['login_page'], selectors['manager_page'],
             selectors['manager_page']['delete_btn5'], selectors['manager_page']['account5_data'])
            # Check if customer_data is in table_before and not in table_after
            assert customer_data in customers_table and \
                   customer_data not in updated_customers_table,\
                   'Customer data was not deleted as expected.'
        except Exception as error:
            # If an exception occurs
            self.take_screenshot(driver, 'test3_error')  # Capture a screenshot
            traceback.print_exc()  # print the error traceback
            raise  # re-raise the exception
        finally:
            # Quit the driver regardless of whether an exception was raised or not
            if driver:
                driver.quit()

    def test4_add_customer(self, url):
        '''
        Test case to simulate adding a customer.
        :param url: The URL of the application.
        '''
        # Initialize the driver outside the try block
        # to ensure it's accessible in the finally block
        driver = None
        try:
            driver = get_driver(url)
            user_data = {
                        'first_name': 'Draco',
                        'last_name': 'Malfoy',
                        'post_code': 'E47832'
                        }
            customers_table, updated_customers_table = add_customer\
            (driver, selectors['login_page'], selectors['manager_page'], user_data)
            for value in user_data.values():
                assert value.lower() in updated_customers_table.lower() and \
                       value not in customers_table.lower(),\
                       'Customer data was not added as expected.'
        except Exception as error:
            # If an exception occurs
            self.take_screenshot(driver, 'test4_error')  # Capture a screenshot
            traceback.print_exc()  # print the error traceback
            raise  # re-raise the exception
        finally:
            # Quit the driver regardless of whether an exception was raised or not
            if driver:
                driver.quit()

    def test5_open_account(self, url):
        '''
        Test case to simulate opening an account.
        :param url: The URL of the application.
        '''
        # Initialize the driver outside the try block
        # to ensure it's accessible in the finally block
        driver = None
        try:
            driver = get_driver(url)
            actual, expected, customer_data, updated_customer_data = open_account\
            (driver, selectors['login_page'], selectors['manager_page'],
             selectors['customer_page']['albus'], selectors['manager_page']['pound'],
             selectors['manager_page']['account4_data'])
            # checking if the url hasn't changed after opening new account
            # and also checking if the length of the updated customer data is bigger than
            # the customers data before opening an account
            assert actual == expected and \
                   len(updated_customer_data) > len(customer_data),\
                   'Account was not opened as expected.'
        except Exception as error:
            # If an exception occurs
            self.take_screenshot(driver, 'test5_error')  # capture a screenshot
            traceback.print_exc()  # print the error traceback
            raise   # re-raise the exception
        finally:
            # Quit the driver regardless of whether an exception was raised or not
            if driver:
                driver.quit()

    def test6_sanity_test(self, url):
        '''
        Test case to perform a sanity test by checking the status code of the application.
        :param url: The URL of the application.
        '''
        # Initialize the driver outside the try block
        # to ensure it's accessible in the finally block
        driver = None
        try:
            driver = get_driver(url)
            status_code = sanity_test(driver)
            assert status_code == 200,\
                   'Sanity test failed. Status code is not as expected.'
        except Exception as error:
            # If an exception occurs
            self.take_screenshot(driver, 'test6_error')  # capture a screenshot
            traceback.print_exc()  # print the error traceback
            raise  # re-raise the exception
        finally:
            # Quit the driver regardless of whether an exception was raised or not
            if driver:
                driver.quit()
