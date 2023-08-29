'''
This file contains all the selectors of the XYZ Bank that I used in my codes.
'''
# user_deposit_selectors = {
#         'customer_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
#         'login_btn': 'body > div > div > div.ng-scope > div > form > button',
#         'deposit_btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
#         'amount_tb': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
#         'balance_number': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)'
#     }
# customer_name_selectors = {
#         'hermione': '#userSelect > option:nth-child(2)',
#         'harry': '#userSelect > option:nth-child(3)',
#         'ron': '#userSelect > option:nth-child(4)',
#         'albus': '#userSelect > option:nth-child(5)',
#         'neville': '#userSelect > option:nth-child(6)'
# }
#
# user_balance_selectors = {
#     'login_page': {
#         'customer_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button'
#     },
#     'customer_page': {
#         'select_customer': {
#             'hermione': '#userSelect > option:nth-child(2)',
#             'harry': '#userSelect > option:nth-child(3)',
#             'ron': '#userSelect > option:nth-child(4)',
#             'albus': '#userSelect > option:nth-child(5)',
#             'neville': '#userSelect > option:nth-child(6)'
#         },
#         'login_btn': 'body > div > div > div.ng-scope > div > form > button'
#     },
#     'account_page': {
#         'deposit_btn': '...',
#         'withdraw_btn': '...',
#         'amount_tb': '...',
#         'balance_number': '...'
#     }
# }
#
# # Selectors for delete_customer function
# delete_customer_selectors = {
#     'login_page': {
#         'manager_login_btn': '...',
#     },
#     'manager_page': {
#         'customers_btn': '...',
#         'customers_table': '...'
#     }
# }
#
# # Selectors for add_customer function
# add_customer_selectors = {
#     'login_page': {
#         'manager_login_btn': '...',
#     },
#     'manager_page': {
#         'customers_btn': '...',
#         'customers_table': '...',
#         'add_customer_btn': '...',
#         'first_name_tb': '...',
#         'last_name_tb': '...',
#         'post_code_tb': '...',
#         'process_btn': '...',
#     }
# }
#
# # Selectors for open_account function
# open_account_selectors = {
#     'login_page': {
#         'manager_login_btn': '...',
#     },
#     'manager_page': {
#         'customers_btn': '...',
#     },
#     'customer_page': {
#         'customer_name_btn': '...',
#         'currency_btn': '...',
#     }
# }
#
# # Selectors for sanity_test function
# sanity_test_selectors = {
#     'login_page': {
#         'manager_login_btn': '...',
#     },
#     'manager_page': {
#         'customers_btn': '...',
#     }
# }

selectors = \
    {
        'login_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
                  'customer_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
                  'manager_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
                  'home_btn': 'body > div > div > div.box.mainhdr > button.btn.home'},
        'customer_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer
                  'hermione': '#userSelect > option:nth-child(2)',
                  'harry': '#userSelect > option:nth-child(3)',
                  'ron': '#userSelect > option:nth-child(4)',
                  'albus': '#userSelect > option:nth-child(5)',
                  'neville': '#userSelect > option:nth-child(6)',
                  'login_btn': 'body > div > div > div.ng-scope > div > form > button'},
        'account_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account
                  'deposit_btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
                  'withdraw_btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
                  'amount_tb': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
                  'balance_number': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)',
                  'currency_type': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(3)',
                  'log_out_btn': 'body > div > div > div.box.mainhdr > button.btn.logout'},
        'manager_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
                  'add_customer_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)',
                  'first_name_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input',
                  'last_name_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input',
                  'post_code_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input',
                  'open_account_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(2)',
                  'dollar': '#currency > option:nth-child(2)',
                  'pound': '#currency > option:nth-child(3)',
                  'rupee': '#currency > option:nth-child(4)',
                  'process_btn': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button',
                  'customers_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
                  'delete_btn1': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button',
                  'delete_btn2': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > button',
                  'delete_btn3': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > button',
                  'delete_btn4': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4) > td:nth-child(5) > button',
                  'delete_btn5': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5) > td:nth-child(5) > button',
                  'customers_table': 'body > div > div > div.ng-scope > div > div.ng-scope > div',
                  'account1_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1)',
                  'account2_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(2)',
                  'account3_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(3)',
                  'account4_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4)',
                  'account5_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5)'}
    }
