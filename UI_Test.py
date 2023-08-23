import pytest
from UIFunctions import *

class TestUI:

    @pytest.fixture
    def url(self):
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'


    def test1_user_deposit(self, url):
        # לשאול את חודי איך לעשות פעם אחת סלקטורים לכל הפונקציות
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
        driver = get_driver(url)
        balance_before, balance_after = user_deposit(driver, selectors, 250)
        assert balance_after == balance_before + 250   # Check if balance increased by 250
        driver.quit()

    def test2_user_balance(self, url):
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
        driver = get_driver(url)
        balance_before, balance_after = user_balance(driver, selectors, 1000, 250)
        assert balance_after == balance_before + 750
        driver.quit()
