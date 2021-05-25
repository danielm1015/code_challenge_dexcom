# Dexcom Coding Challenge
Python Web Automation using Page Object Oriented Design for Dexcom coding challenge using the behave framework.
## Prerequisites

Python intallation: https://www.python.org/downloads/ 
* Tested on Python 3.7

Behave installation: https://behave.readthedocs.io/en/stable/install.html

Chrome driver isntallation: https://chromedriver.chromium.org/downloads
* Tested on chromedriver version 90 used

## Running the Behave test
* Clone Repo
* cd into directory with features and steps
* run on cmd line:  ```behave````

behave Command-Line Arguments: https://behave.readthedocs.io/en/stable/behave.html



## API Testing

### Test Steps:
1. Start with a GET call to https://clarity.dexcom.com
2. Login with username and password 
a. Do not hardcode access-token, access-token should be retrieved from dynamic
server response after login.
3. Make HTTP POST request call to "/api/subject/1681277794575765504/analysis_session"
4. Assert analysisSessionId should not be None


Was unable to get Access-Token through API calls, but i was able to locate it in Network tabs.
Attempted to capture redirects that contained response headers and cookies that were in response for the Access-Token
I was able to get 200 response codes, and the content was error html that did not contain token
I was using the Python REPL for this test

```
import os
import requests


session = requests.session()
session.get("https://clarity.dexcom.com/")
response = _session.get("https://clarity.dexcom.com/users/auth/dexcom_sts")
assert response.status_code == 200, f'Bad response: {response.status_code} {response.reason}'

redirect1 = response.history[1].url
redirect2 = response.url

for c in _session.cookies:
    if c.name == 'idsrv.xsrf':
		_cookie = c

assert cookie, "Cookie not found"
isdrv_xsrf = _cookie.value

session.get("https://uam1.dexcom.com")

_data = {"username": os.environ["demo"], "password": os.environ["demopass"]:, "isdrv_xsrf": isdrv_xsrf}
_headers = {"Content-Type": "x-www-form-urlencoded"}
response2 = _session.post(_redirect2, data= _data, headers= _headers)
assert response2.status_code == 200, f'Bad response: {response.status_code} {response.reason}'

```