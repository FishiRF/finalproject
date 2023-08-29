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
            print(f'Error URL {error}')
            traceback.print_exc()
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
            with open('error_log.txt', 'a+') as file:
                file.write(f'Test: {test_name}\n')
                file.write(f'Time: {current_time}\n')
                file.write(f'Error: {error_msg}\n\n')
        except Exception as error:
            print(f'An error occurred while logging: {error}')
            traceback.print_exc()

    def test1_user_data_P(self, url):
        '''
        Test retrieving user data with a valid user ID.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            status_code, user_data = get_user_data(url, 'user/1')
            assert status_code < 400 and user_data is not None, \
                'User data retrieval failed with a valid user ID.'
        except Exception as error:
            self.log_error('test1_user_data_P', str(error))
            traceback.print_exc()

    def test2_user_data_N(self, url):
        '''
        Test retrieving user data with an invalid user ID.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            msg = '404 Client Error: Not Found for url: https://reqres.in/api/user/999'
            status_code, user_data = get_user_data(url, 'user/999')
            assert status_code >= 400 and user_data == msg, \
                'User data retrieval succeeded with an invalid user ID.'
        except Exception as error:
            self.log_error('test2_user_data_N', str(error))  # Log the actual error message
            traceback.print_exc()

    def test3_create_user(self, url):
        '''
        Test creating a new user with valid data.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            data = {
                'name': 'morpheus',
                'job': 'leader'
            }
            status_code, user_data = create_user(url, 'users', data)
            assert status_code < 400 and user_data['name'] == data['name'] \
                   and user_data['job'] == data['job'], \
                'User creation failed with valid data.'
        except Exception as error:
            self.log_error('test3_create_user', str(error))
            traceback.print_exc()

    def test4_user_login_P(self, url):
        '''
        Test user login with valid credentials.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            data = {
                'email': 'eve.holt@reqres.in',
                'password': 'cityslicka'
            }
            status_code, token = user_login(url, 'login', data)
            assert status_code < 400 and token is not None, \
                'User login failed with valid credentials.'
        except Exception as error:
            self.log_error('test4_user_login_P', str(error))
            traceback.print_exc()

    def test5_user_login_N(self, url):
        '''
        Test user login with invalid credentials.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            data = {
                'email': 'peter@klaven'
            }
            status_code, token = user_login(url, 'login', data)
            assert status_code >= 400 or token is None, \
                'User login succeeded with invalid credentials.'
        except Exception as error:
            self.log_error('test5_user_login_N', str(error))
            traceback.print_exc()

    def test6_invalid_http_method(self, url):
        '''
        Test handling of invalid HTTP method.
        :param url: The base URL of the API.
        :return: None
        '''
        try:
            status_code = invalid_http_method(url, 'user')
            assert status_code >= 400, \
                f'Invalid HTTP method not handled correctly {status_code}'
        except Exception as error:
            self.log_error('test6_invalid_http_method', str(error))
            traceback.print_exc()
