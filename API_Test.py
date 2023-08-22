import pytest
from APIFunctions import *

class TestAPI:

    @pytest.fixture()
    def url(self):
        '''
        :return: the function returns the req-res website url for the users page
        '''
        return 'https://reqres.in/api/'

    def test1_user_data_P(self, url):
        '''
        :param url: this parameter represents the req-res website url
        :return: the function tests if the user exists
                 and if the website contains the user's data
        '''
        status_code, user_data = get_existing_user(url, 'user/1')
        assert status_code < 400 and user_data is not None, "User doesn't exists"

    def test2_user_data_N(self, url):
        '''
        :param url: this parameter represents the req-res website url
        :return: the function tests the case for a none-existing user
                 and checks if the website contains no data
        '''
        status_code, user_data = get_existing_user(url, 'user/999')
        # the file is not empty but showing only {}
        assert status_code >= 400 and user_data == {}

    def test3_create_user(self, url):
        data = {
                "name": "morpheus",
                "job": "leader"
                }
        status_code, user_data = create_user(url, 'users', data)
        assert status_code < 400 and user_data['name'] == data['name']\
               and user_data['job'] == data['job'], 'Data is invalid'

    def test4_user_login_P(self, url):
        data = {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
                }
        status_code, token = user_login(url, 'login', data)
        assert status_code < 400 and token is not None, 'Bad credentials'

    def test5_user_login_N(self, url):
        data = {
                "email": "peter@klaven"
                }
        status_code, token = user_login(url, 'login', data)
        assert status_code >= 400 or token is None

    def test6_invalid_http_method(self, url):
        status_code = invalid_http_method(url, 'user')
        assert status_code >= 400, f'Invalid HTTP method not handled correctly{status_code}'


