import pytest
from UIFunctions import *
from Bank_Selectors import *
class TestUI:
# add try except to every test function
    @pytest.fixture
    def url(self):
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def test1_user_deposit(self, url, selectors):
        # לשאול את חודי איך לעשות פעם אחת סלקטורים לכל הפונקציות
        # selectors = {
        #     'customer_login': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
        #     'hermione': '#userSelect > option:nth-child(2)',
        #     'login_btn': 'body > div > div > div.ng-scope > div > form > button',
        #     'deposit_btn1': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
        #     'amount_tb': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
        #     'deposit_btn2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
        #     'withdraw_btn1': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
        #     'amount_tb2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
        #     'withdraw_btn2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
        #     'balance': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)'
        # }
        # accounts_selectors = {
        #     'hermione': '#userSelect > option:nth-child(2)',
        #     'harry': '#userSelect > option:nth-child(3)',
        #     'ron': '#userSelect > option:nth-child(4)',
        #     'albus': '#userSelect > option:nth-child(5)',
        #     'neville': '#userSelect > option:nth-child(6)'
        }
        driver = get_driver(url)
        balance_before, balance_after = user_deposit(driver, selectors['customer_selectors']['hermione'], 250)
        assert balance_after == balance_before + 250   # Check if balance increased by 250
        driver.quit()

    def test2_user_balance(self, url, selectors):
        selectors = {
            'customer_login': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
            'hermione': '#userSelect > option:nth-child(2)',
            'login_btn': 'body > div > div > div.ng-scope > div > form > button',
            'deposit_btn1': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
            'amount_tb': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
            'deposit_btn2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
            'withdraw_btn1': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
            'amount_tb2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
            'withdraw_btn2': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
            'balance': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)'
        }
        accounts_selectors = {
            'hermione': '#userSelect > option:nth-child(2)',
            'harry': '#userSelect > option:nth-child(3)',
            'ron': '#userSelect > option:nth-child(4)',
            'albus': '#userSelect > option:nth-child(5)',
            'neville': '#userSelect > option:nth-child(6)'
        }
        driver = get_driver(url)
        balance_before, balance_after = user_balance(driver, selectors, accounts_selectors['ron'], 1000, 250)
        assert balance_after == balance_before + 750

        driver.quit()

    def test3_delete_customer(self, url, selectors):
        selectors = {
                     'manager_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
                     'customers_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
                     'delete_neville_btn': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5) > td:nth-child(5) > button',
                     'customers_table': 'body > div > div > div.ng-scope > div > div.ng-scope > div'
                     }
        delete_customers_selectors = {
            'delete_hermione': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button',
            'delete_harry': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > button',
            'delete_ron': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > button',
            'delete_albus': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4) > td:nth-child(5) > button',
            'delete_neville': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5) > td:nth-child(5) > button'
        }
        driver = get_driver(url)
        table_before, table_after = delete_customer(driver, selectors, delete_customers_selectors['neville'])
        assert table_after != table_before # also check if the user doesn't appear in the table
        # another option - לשאול את חודי מה יותר נכון
        # assert len(table_after) < len(table_before)

        driver.quit()

    def test4_add_customer(self, url, selectors):
        driver = get_driver(url)
        selectors = {
                    'manager_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
                    'customers_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
                    'delete_neville_btn': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5) > td:nth-child(5) > button',
                    'customers_table': 'body > div > div > div.ng-scope > div > div.ng-scope > div',
                    'add_customer_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)',
                    'first_name_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input',
                    'last_name_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input',
                    'post_code_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input',
                    'add_customer_btn2': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button'
                    }
        user_data = {
                    'first_name': 'Draco',
                    'last_name': 'Malfoy',
                    'post_code': 'E47832'
                    }
        table_before, table_after = add_customer(driver, selectors, user_data)
     # and also make sure the user appear in the table
        assert len(table_after) > len(table_before)

        driver.quit()

    def test5_open_account(self, url, selectors):
        driver = get_driver(url)
        selectors = {
                    'manager_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
                    'open_account_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(2)',
                    'process_btn': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button',
                    'customers_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
                    'albus_num_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4) > td:nth-child(4)',
                    'home_btn': 'body > div > div > div.box.mainhdr > button.btn.home',
                    'customer_login': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
                    'login_btn': 'body > div > div > div.ng-scope > div > form > button',
                    'account_number_btn': '#accountSelect > option:nth-child(4)',
                    'currency_type': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(3)'
                    }
        accounts_selectors = {
                              'hermione': '#userSelect > option:nth-child(2)',
                              'harry': '#userSelect > option:nth-child(3)',
                              'ron': '#userSelect > option:nth-child(4)',
                              'albus': '#userSelect > option:nth-child(5)',
                              'neville': '#userSelect > option:nth-child(6)'
                              }
        currency_selectors = {
                              'dollar': '#currency > option:nth-child(2)',
                              'pound': '#currency > option:nth-child(3)',
                              'rupee': '#currency > option:nth-child(4)',
                              }
        actual = open_account(driver, selectors, accounts_selectors['albus'], currency_selectors['pound'])
        assert actual != url    # change here the url to the urlbefore opening account and after opening account

    def test6_sanity_test(self, url):
        driver = get_driver(url)
        try:
            # Test 1: Check user deposit functionality
            self.test1_user_deposit(url)
            # Test 2: Check user balance functionality
            self.test2_user_balance(url)
            # Test 3: Check customer deletion functionality
            self.test3_delete_customer(url)
            # Test 4: Check customer addition functionality
            self.test4_add_customer(url)
            # Test 5: Check account addition functionality and URL change
            self.test5_open_account(url)
        finally:
            # close the browser
            driver.quit()
