import pytest
from APIFunctions import *

class TestAPI:

    @pytest.fixture()
    def url(self):
        '''
        Get the base URL of the API.
        :return: The base URL of the API.
        '''
        return 'https://reqres.in/api/'

    def test1_user_data_P(self, url):
        '''
        Test retrieving user data with a valid user ID.
        :param url: The base URL of the API.
        :return: None
        '''
        status_code, user_data = get_user_data(url, 'user/1')
        assert status_code < 400 and user_data is not None, "User doesn't exists"

    def test2_user_data_N(self, url):
        '''
        Test retrieving user data with an invalid user ID.
        :param url: The base URL of the API.
        :return: None
        '''
        status_code, user_data = get_user_data(url, 'user/999')
        # the file is not empty but showing only {}
        assert status_code >= 400 and user_data == {}

    def test3_create_user(self, url):
        '''
        Test creating a new user with valid data.
        :param url: The base URL of the API.
        :return: None
        '''
        data = {
                "name": "morpheus",
                "job": "leader"
                }
        status_code, user_data = create_user(url, 'users', data)
        assert status_code < 400 and user_data['name'] == data['name']\
               and user_data['job'] == data['job'], 'Data is invalid'

    def test4_user_login_P(self, url):
        '''
        Test user login with valid credentials.
        :param url: The base URL of the API.
        :return: None
        '''
        data = {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
                }
        status_code, token = user_login(url, 'login', data)
        assert status_code < 400 and token is not None, 'Bad credentials'

    def test5_user_login_N(self, url):
        '''
        Test user login with invalid credentials.
        :param url: The base URL of the API.
        :return: None
        '''
        data = {
                "email": "peter@klaven"
                }
        status_code, token = user_login(url, 'login', data)
        assert status_code >= 400 or token is None

    def test6_invalid_http_method(self, url):
        '''
        Test handling of invalid HTTP method.
        :param url: The base URL of the API.
        :return: None
        '''
        status_code = invalid_http_method(url, 'user')
        assert status_code >= 400, f'Invalid HTTP method not handled correctly {status_code}'


