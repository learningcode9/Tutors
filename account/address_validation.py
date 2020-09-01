import requests
from requests_oauthlib import OAuth1
import json


# response=requests.get(
# 'https://us-street.api.smartystreets.com',
# auth_id="9a7b8041-9ac4-7e15-75b0-780771fc3d92",
# auth_token = "xMvDBs26P88X0Esk8q5D",
# # Content-Type:'application/json; charset=utf-8',
# params={'addressee':'Sravani Bellam','street':'7011 Sunne ln','city':'walnut creek','state':'CA','zipcode':94597}
# )

url='https://us-street.api.smartystreets.com'

auth = OAuth1('9a7b8041-9ac4-7e15-75b0-780771fc3d92', 'xMvDBs26P88X0Esk8q5D')

params={'addressee':'Sravani Bellam','street':'7011 Sunne ln','city':'walnut creek','state':'CA','zipcode':94597}


r=requests.get(url=url,auth=auth,params=params)

# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')

# print(r.url)
data=json.loads(r.text)
print(data)


    