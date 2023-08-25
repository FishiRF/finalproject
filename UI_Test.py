import pytest
from UIFunctions import *
from Bank_Selectors import *

class TestUI:
    # add try except to every test function
    @pytest.fixture
    def url(self):
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def test1_user_deposit(self, url):
        driver = get_driver(url)
        balance, updated_balance = user_deposit\
        (driver, selectors['login_page'], selectors['customer_page'],
         selectors['account_page'], selectors['customer_page']['hermione'], 250)
        # Check if balance increased by 250
        assert updated_balance == balance + 250
        driver.quit()

    def test2_user_balance(self, url):
        driver = get_driver(url)
        balance, updated_balance = user_balance\
        (driver, selectors['login_page'], selectors['customer_page'],
         selectors['account_page'], selectors['customer_page']['ron'], 1000, 250)
        # Check if balance increased by 750
        assert updated_balance == balance + 750

        driver.quit()

    def test3_delete_customer(self, url):
        driver = get_driver(url)
        customers_table, updated_customers_table, customer_data = delete_customer\
        (driver, selectors['login_page'], selectors['manager_page'],
         selectors['manager_page']['delete_btn5'], selectors['manager_page']['account5_data'])
        # Check if customer_data is in table_before and not in table_after
        assert customer_data in customers_table and customer_data not in updated_customers_table

        driver.quit()

    def test4_add_customer(self, url):
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
                   value not in customers_table.lower()
        driver.quit()

    def test5_open_account(self, url):
        driver = get_driver(url)
        actual, expected, customer_data, updated_customer_data = open_account\
        (driver, selectors['login_page'], selectors['manager_page'],
         selectors['customer_page']['albus'], selectors['manager_page']['pound'],
         selectors['manager_page']['account4_data'])
        # checking if the url hasn't changed after opening new account
        # and also checking if the length of the updated customer data is bigger than
        # the customers data before opening an account
        assert actual == expected and len(updated_customer_data) > len(customer_data)

    def test6_sanity_test(self, url):
        driver = get_driver(url)
        status_code = sanity_test(driver)
        assert status_code == 200
        driver.quit()