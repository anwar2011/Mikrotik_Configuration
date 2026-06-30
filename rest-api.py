
import requests
from requests.auth import HTTPBasicAuth
import simplejson
import urllib3
urllib3.disable_warnings()
url = 'http://10.248.27.226/rest'
username = 'admin'
password = '1234'
response = requests.get(url+'/ip/address', auth=HTTPBasicAuth(username,password), verify=False)
for interface in response.json():
    print(interface)