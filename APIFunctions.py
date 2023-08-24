import requests

# Get Existing User:
# 	Description: Test if you can retrieve details of an existing user.
# 	Request: GET https://reqres.in/api/user/1
# 	Expected Result: Response status code should be 200 and contain user data.
# Get Nonexistent User:
# 	Description: Test if the API responds correctly when attempting to retrieve a nonexistent user.
# 	Request: GET https://reqres.in/api/user/999
# 	Expected Result: Response status code should be 404.
# ----------------------------------------------------------------------------
def get_user_data(url, user_id):
    '''
    Retrieve user data by sending a GET request to the specified URL.
    :param url: The base URL of the API.
    :param user_id: The ID of the user to retrieve.
    :return: A tuple containing the HTTP status code
             and the user data retrieved from the response.
    '''
    res = requests.get(url + user_id)
    data = res.json()
    if 'data' in data:
        user_data = data['data']
    else:
        user_data = data
    return res.status_code, user_data

# ----------------------------------------------------------------------------
# Create User:
# 	Description: Test if you can successfully create a new user.
# 	Request: POST https://reqres.in/api/user with JSON payload containing user data.
# 	Expected Result: Response status code should be 201, and the returned data should match the submitted data.
def create_user(url, users, user_data):
    '''
    Create a new user by sending a POST request to the specified URL.
    :param url: The base URL of the API.
    :param users: The endpoint for creating users.
    :param user_data: The data representing the user to be created.
    :return: A tuple containing the HTTP status code and the JSON response data.
    '''
    res = requests.post(url + users, data=user_data)
    return res.status_code, res.json()

# ----------------------------------------------------------------------------
# Login Successful:
# 	Description: Test if you can successfully log in with valid credentials.
# 	Request: POST https://reqres.in/api/login with valid login data.
# 	Expected Result: Response status code should be 200, and a token should be present in the response.
# Login Unsuccessful:
# 	Description: Test if login fails with incorrect credentials.
# 	Request: POST https://reqres.in/api/login with incorrect login data.
# 	Expected Result: Response status code should be 400.
def user_login(url, login, user_data):
    '''
    Perform user login by sending a POST request to the specified URL.
    :param url: The base URL of the API.
    :param login: The endpoint for user login.
    :param user_data: The data representing the user's login credentials.
    :return: A tuple containing the HTTP status code and the JSON response data.
    '''
    res = requests.post(url + login, data=user_data)
    return res.status_code, res.json()

# ----------------------------------------------------------------------------
# Invalid Method:
# 	Description: Test if the API handles invalid HTTP methods appropriately.
# 	Request: PUT https://reqres.in/api/user
# 	Expected Result: Response status code should be 405 (Method Not Allowed).
def invalid_http_method(url, user):
    '''
    Send an invalid HTTP method request to the specified URL for a user.
    :param url: The base URL of the API.
    :param user: The user endpoint or identifier.
    :return: The HTTP status code of the response.
    '''
    res = requests.put(url + user)
    return res.status_code











