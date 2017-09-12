import json
import jwt
import time
import hashlib
import requests


# from jwt import *

def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


def n_test():
    # USER
    USER = 'bhakti.thakkar'

    # ACCESS KEY from navigation >> Tests >> API Keys
    ACCESS_KEY = 'NWExYWRiNTUtMDdkZi0zNjhkLWI4MzMtMzQzZjU1NDZmOWM2IGJoYWt0aS50aGFra2FyIGJoYWt0aS50aGFra2Fy'

    # ACCESS KEY from navigation >> Tests >> API Keys
    SECRET_KEY = 'FYx1MGlGqf-MDvxM3C5jtDHXXqZgUey3RIKD9b68uNE'

    # JWT EXPIRE how long token been to be active? 3600 == 1 hour/
    JWT_EXPIRE = 3600

    # BASE URL for Zephyr for Jira Cloud
    BASE_URL = 'https://calcuquote.atlassian.net'

    # RELATIVE PATH for token generation and make request to api
    RELATIVE_PATH = '/public/rest/api/1.0/cycle'

    # CANONICAL PATH (Http Method & Relative Path & Query String)
    CANONICAL_PATH = 'POST&' + RELATIVE_PATH + '&'

    # TOKEN HEADER: to generate jwt token
    payload_token = {
        'sub': USER,
        'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
        'iss': ACCESS_KEY,
        'exp': int(time.time()) + JWT_EXPIRE,
        'iat': int(time.time())
    }

    # GENERATE TOKEN
    token = jwt.encode(payload_token, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

    # REQUEST HEADER: to authenticate and authorize api
    headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
        'zapiAccessKey': ACCESS_KEY
    }

    # REQUEST HEADER: to create cycle
    headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
        'zapiAccessKey': ACCESS_KEY
    }

    # REQUEST PAYLOAD: to create cycle
    cycle = {
        'name': 'Sample Cycle',
        'projectId': 10000,
        'versionId': -1
    }

    # MAKE REQUEST:
    raw_result = requests.post(BASE_URL + RELATIVE_PATH, headers=headers, json=cycle)
    if is_json(raw_result.text):

        # JSON RESPONSE: convert response to JSON
        json_result = json.loads(raw_result.text)

        # PRINT RESPONSE: pretty print with 4 indent
        print(json.dumps(json_result, indent=4, sort_keys=True))

    else:
        print(raw_result.text)


if __name__ == '__main__':
    n_test()
