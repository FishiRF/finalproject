import pytest
from APIFunctions import *
from datetime import datetime

class TestAPI:
    @pytest.fixture()
    def url(self):
        '''
        Get the base URL of the API.
        :return: The base URL of the API.
        '''
        try:
            return 'https://reqres.in/api/'
        except Exception as error:
            print(f'Error url {error}')
            return None

    def log_error(self, test_name, error_msg):
        '''
        Log error information to a file.
        :param test_name: The name of the test that encountered the error.
        :param error_msg: The error message to be logged.
        :return: None
        '''
        try:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open('error_log.txt','a+') as file:
                file.write(f'Test: {test_name}\n')
                file.write(f'Time: {current_time}\n')
                file.write(f'Error:{error_msg}\n\n')
        except Exception as error:
            print(f'An error occurred while logging: {error}')

    def test1_update_user(self, url):
        '''
        Test function for updating a user's information.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            data = {"name": "morpheus",
                    "job": "zion resident"}
            status_code, update_data = update_user(url,'users/2',data)
            assert status_code < 400 and update_data['name'] == data['name'] and update_data['job'] == data['job'],\
                'Update user failed'
        except Exception as error:
            self.log_error('test1_update_user', str(error))

    def test2_partial_update_user(self, url):
        '''
        Test function for partially updating a user's information.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            data = {"name": "morpheus",
                    "job": "zion resident"}
            status_code, update_data = update_user(url,'users/1',data)
            assert status_code < 400 and update_data['name'] == data['name'] and update_data['job'] == data['job'],\
                'Partial update user failed'
        except Exception as error:
            self.log_error('test2_partial_update_user', str(error))

    def test3_delete_user(self, url):
        '''
        Test function for deleting a user.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            status_code = delete_user(url, 'users/3')
            assert status_code < 400, 'user delete failed'
        except Exception as error:
            self.log_error('test3_delete_user', str(error))

    def test4_list_user(self, url):
        '''
        Test function for listing users.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            list_status_code, list1 = list_user(url, 'users/')
            list_status_code, list2 = list_user(url, 'users?page=2')
            lists = list1+list2
            assert list_status_code < 400 and len(lists) == 12, \
                'The list is not shown as expected'
        except Exception as error:
            self.log_error('test4_list_user', str(error))

    def test5_register_P(self, url):
        '''
        Test function for registering a user with valid data.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            data = {"email": "eve.holt@reqres.in",
                    "password": "pistol"}
            register_status_code , register = user_register(url,'register',data)
            assert register_status_code < 400 and register is not {}, 'Register test failed using valid data'
        except Exception as error:
            self.log_error('test5_register_P', str(error))

    def test6_register_N(self, url):
        '''
        Test function for registering a user with invalid data.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            data = {"email": "sydney@fife"}
            register_status_code, register = user_register(url, 'register', data)
            assert register_status_code >= 400, 'Register test failed using invalid data'
        except Exception as error:
            self.log_error('test6_register_N', str(error))
