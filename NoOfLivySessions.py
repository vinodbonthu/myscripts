import json
import requests
import urllib2
from io import BytesIO
import pprint
import pycurl

curl = pycurl.Curl()
data = BytesIO()

curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_GSSNEGOTIATE)
#curl.setopt(pycurl.PROXYUSERPWD, str("%s:%s" % (proxy["username"], proxy["password"])))
#curl.setopt(pycurl.USERPWD, '%s:%s' % (username, password))
curl.setopt(pycurl.USERPWD, ':')
curl.setopt(pycurl.HTTPHEADER, ['X-Postmark-Server-Token: API_TOKEN_HERE','Accept: application/json'])
curl.setopt(pycurl.URL, 'http://172.26.92.157:8998/sessions')
curl.setopt(pycurl.WRITEFUNCTION, data.write)
curl.perform()

dictionary = json.loads(data.getvalue())
pprint.pprint(dictionary["total"])

