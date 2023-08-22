import requests

# Get Existing User:
# 	Description: Test if you can retrieve details of an existing user.
# 	Request: GET https://reqres.in/api/user/1
# 	Expected Result: Response status code should be 200 and contain user data.

def get_existing_user(url, user_id):
    '''
    :param url: this parameter represents the req-res website url
    :param user_id: this parameter represents the user's id number
    :return: the function returns the response status code and the user's data
    '''
    res = requests.get(url + user_id)
    data = res.json()
    if 'data' in data:
        user_data = data['data']
    else:
        user_data = data
    return res.status_code, user_data

# ----------------------------------------------------------------------------
# Get Nonexistent User:
# 	Description: Test if the API responds correctly when attempting to retrieve a nonexistent user.
# 	Request: GET https://reqres.in/api/user/999
# 	Expected Result: Response status code should be 404.
# ----------------------------------------------------------------------------
# Create User:
# 	Description: Test if you can successfully create a new user.
# 	Request: POST https://reqres.in/api/user with JSON payload containing user data.
# 	Expected Result: Response status code should be 201, and the returned data should match the submitted data.
def create_user(url, users, user_data):
    res = requests.post(url + users, data=user_data)
    return res.status_code, res.json()

# ----------------------------------------------------------------------------
# Login Successful:
# 	Description: Test if you can successfully log in with valid credentials.
# 	Request: POST https://reqres.in/api/login with valid login data.
# 	Expected Result: Response status code should be 200, and a token should be present in the response.
def user_login(url, login, user_data):
    res = requests.post(url + login, data=user_data)
    return res.status_code, res.json()

# ----------------------------------------------------------------------------
# Login Unsuccessful:
# 	Description: Test if login fails with incorrect credentials.
# 	Request: POST https://reqres.in/api/login with incorrect login data.
# 	Expected Result: Response status code should be 400.
# ----------------------------------------------------------------------------
# Invalid Method:
# 	Description: Test if the API handles invalid HTTP methods appropriately.
# 	Request: PUT https://reqres.in/api/user
# 	Expected Result: Response status code should be 405 (Method Not Allowed).
def invalid_http_method(url, user):
    res = requests.put(url + user)
    return res.status_code











