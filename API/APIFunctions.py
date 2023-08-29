import requests
import traceback
def get_user_data(url, user_id):
    '''
    Retrieve user data by sending a GET request to the specified URL.
    :param url: The base URL of the API.
    :param user_id: The ID of the user to retrieve.
    :return: A tuple containing the HTTP status code
             and the user data retrieved from the response.
    '''
    try:
        res = requests.get(url + user_id)
        res.raise_for_status()  # raise HTTP error for bad responses (400+, 500+)
        data = res.json()
        if 'data' in data:
            user_data = data['data']
        else:
            user_data = data
        return res.status_code, user_data
    except Exception as error:
        traceback.print_exc()
        return f'status code {500}', str(error)  # return a custom error status and message

def create_user(url, users, user_data):
    '''
    Create a new user by sending a POST request to the specified URL.
    :param url: The base URL of the API.
    :param users: The endpoint for creating users.
    :param user_data: The data representing the user to be created.
    :return: A tuple containing the HTTP status code and the JSON response data.
    '''
    try:
        res = requests.post(url + users, json=user_data)
        res.raise_for_status()  # raise HTTP error for bad responses (400+, 500+)
        return res.status_code, res.json()
    except Exception as error:
        traceback.print_exc()
        return f'status code {500}', str(error)  # return a custom error status and message

def user_login(url, login, user_data):
    '''
    Perform user login by sending a POST request to the specified URL.
    :param url: The base URL of the API.
    :param login: The endpoint for user login.
    :param user_data: The data representing the user's login credentials.
    :return: A tuple containing the HTTP status code and the JSON response data.
    '''
    try:
        res = requests.post(url + login, json=user_data)
        res.raise_for_status()  # raise HTTP error for bad responses (400+, 500+)
        return res.status_code, res.json()
    except Exception as error:
        traceback.print_exc()
        return f'status code {500}', str(error)  # return a custom error status and message

def invalid_http_method(url, user):
    '''
    Send an invalid HTTP method request to the specified URL for a user.
    :param url: The base URL of the API.
    :param user: The user endpoint or identifier.
    :return: The HTTP status code of the response.
    '''
    try:
        res = requests.put(url + user)
        return res.status_code
    except Exception as error:
        traceback.print_exc()
        return f'status code {500} {str(error)}'  # return a custom error status and message
