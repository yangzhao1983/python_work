import http.client
from urllib import parse
import ssl
import json
from ftplib import FTP

# rest request
conn= http.client.HTTPSConnection("qatenant17.identity.env6.ociqa1.c9dev1.oc9qadev.com",443,context=ssl._create_unverified_context())
conn.set_debuglevel(1)
token = 'eyJ4NXQjUzI1NiI6Im9XQ184dFRkeEk0WFdxbTFldWNxU1Foanhiam11QUF3NVhwYlhrUGw5X0EiLCJ4NXQiOiJVbmt0NUFkcFMwX3hCTDd3WFNXdkxhdFlrYmsiLCJraWQiOiJTSUdOSU5HX0tFWSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ0ZXN0QWRtaW5DbGllbnRfeXpDbWFfQVBQSUQiLCJ1c2VyLnRlbmFudC5uYW1lIjoiUUFURU5BTlQxNyIsInN1Yl9tYXBwaW5nYXR0ciI6InVzZXJOYW1lIiwiaXNzIjoiaHR0cHM6XC9cL2lkZW50aXR5Lm9yYWNsZWNsb3VkLmNvbVwvIiwidG9rX3R5cGUiOiJBVCIsImNsaWVudF9pZCI6InRlc3RBZG1pbkNsaWVudF95ekNtYV9BUFBJRCIsImF1ZCI6WyJodHRwczpcL1wvUUFURU5BTlQxNy5pZGVudGl0eS5lbnY2Lm9jaXFhMS5jOWRldjEub2M5cWFkZXYuY29tOjQ0MyIsInVybjpvcGM6bGJhYXM6bG9naWNhbGd1aWQ9UUFURU5BTlQxNyJdLCJzdWJfdHlwZSI6ImNsaWVudCIsImNsaWVudEFwcFJvbGVzIjpbIkdsb2JhbCBWaWV3ZXIiLCJBdXRoZW50aWNhdGVkIENsaWVudCIsIklkZW50aXR5IERvbWFpbiBBZG1pbmlzdHJhdG9yIiwiTWUiXSwic2NvcGUiOiJ1cm46b3BjOmlkbTpnLmlkZW50aXR5c291cmNldGVtcGxhdGVfciB1cm46b3BjOmlkbTp0Lmdyb3Vwcy5tZW1iZXJzIHVybjpvcGM6aWRtOnQuYXBwIHVybjpvcGM6aWRtOnQudXNlci5sb2NrZWRzdGF0ZWNoYW5nZXIgdXJuOm9wYzppZG06dC5pZGJyaWRnZS5hZG1pbiB1cm46b3BjOmlkbTp0LnRlcm1zb2Z1c2UgdXJuOm9wYzppZG06dC5pZGNzcnB0cyB1cm46b3BjOmlkbTp0LnJlcXVlc3RzIHVybjpvcGM6aWRtOnQuc2VjdXJpdHkuY2xpZW50IHVybjpvcGM6aWRtOmcuYXBwdGVtcGxhdGVfciB1cm46b3BjOmlkbTp0LmJ1bGsudXNlciB1cm46b3BjOmlkbTp0LmRpYWdub3N0aWNzX3IgdXJuOm9wYzppZG06dC5pZGJfY29udGFpbmVycyB1cm46b3BjOmlkbTp0LmlkYnJpZGdlLnVzZXIgdXJuOm9wYzppZG06dC51c2VyLm1lIHVybjpvcGM6aWRtOmcuYWxsX3IgdXJuOm9wYzppZG06dC51c2VyLnNlY3VyaXR5IHVybjpvcGM6aWRtOnQuYXVkaXRfciB1cm46b3BjOmlkbTp0LmpvYi5hcHAgdXJuOm9wYzppZG06dC5vYXV0aGNvbnNlbnRzIHVybjpvcGM6aWRtOnQuc29taSB1cm46b3BjOmlkbTpnLnNoYXJlZGZpbGVzIHVybjpvcGM6aWRtOnQucmVzLmltcG9ydGV4cG9ydCB1cm46b3BjOmlkbTp0LmpvYi5pZGVudGl0eSB1cm46b3BjOmlkbTp0LnNhbWwgdXJuOm9wYzppZG06dC5tZmEgdXJuOm9wYzppZG06dC5kYi5hZG1pbiB1cm46b3BjOmlkbTp0LnNjaGVtYXMgdXJuOm9wYzppZG06dC5tZmEudXNlcmFkbWluIHVybjpvcGM6aWRtOnQub2F1dGggdXJuOm9wYzppZG06dC5ncm91cHMgdXJuOm9wYzppZG06dC5qb2IuaW1wb3J0ZXhwb3J0IHVybjpvcGM6aWRtOnQuaWRicmlkZ2UudW5tYXBwZWQuaWRjc2F0dHJpYnV0ZXMgdXJuOm9wYzppZG06dC5rcmIuYWRtaW4gdXJuOm9wYzppZG06dC5uYW1lZGFwcGFkbWluIHVybjpvcGM6aWRtOnQuYmxrcnB0cyB1cm46b3BjOmlkbTp0LnNlbGZyZWdpc3RyYXRpb25wcm9maWxlIHVybjpvcGM6aWRtOnQudXNlci5hdXRoZW50aWNhdGUgdXJuOm9wYzppZG06dC5ncmFudHMgdXJuOm9wYzppZG06dC5hdXRoZW50aWNhdGlvbiB1cm46b3BjOmlkbTp0LmNvbnRhaW5lciB1cm46b3BjOmlkbTp0LmltYWdlcyB1cm46b3BjOmlkbTp0LmJ1bGsgdXJuOm9wYzppZG06dC5qb2Iuc2VhcmNoIHVybjpvcGM6aWRtOnQuaWRicmlkZ2UgdXJuOm9wYzppZG06dC5hcHBzZXJ2aWNlcyB1cm46b3BjOmlkbTp0LnNldHRpbmdzIHVybjpvcGM6aWRtOnQuaWRicmlkZ2Uuc291cmNlZXZlbnQgdXJuOm9wYzppZG06dC5wb2xpY3kgdXJuOm9wYzppZG06dC51c2VycyB1cm46b3BjOmlkbTp0LnJlcG9ydHMgdXJuOm9wYzppZG06Zy5pZGNzcnB0c21ldGFfciIsImNsaWVudF90ZW5hbnRuYW1lIjoiUUFURU5BTlQxNyIsImV4cCI6MTU0NTc3OTU3MiwiaWF0IjoxNTQzOTc5NTcyLCJ0ZW5hbnRfaXNzIjoiaHR0cHM6XC9cL1FBVEVOQU5UMTcuaWRlbnRpdHkuZW52Ni5vY2lxYTEuYzlkZXYxLm9jOXFhZGV2LmNvbTo0NDMiLCJjbGllbnRfZ3VpZCI6IjM2NjQxZjBhYzZlMzRkOGM5NWRiNmI3OTc5ODAwNTEyIiwiY2xpZW50X25hbWUiOiJ0ZXN0QWRtaW5DbGllbnRfeXpDbWEiLCJ0ZW5hbnQiOiJRQVRFTkFOVDE3IiwianRpIjoiZWI3YjExN2UtODFlYi00YTU1LWJmNjctZDVjYmQyZWI1NzhlIn0.TWsNEG4Tmb11Bb95jexYSaXHX58kCNd8WhkEzvPAMCV0PyELRxuK9ipngey5re9vl_U8l-EbaiD3IqxVMYcjXvG_atSWfaw_fhVn15jVSOEKko_6n-0sdnw26vMc2a8htpOcUX_l-JrlxdUUfP6E2X4HnAM1gpofW8zCUjE33ixIK7CigkP8xiW9SbqrmB6lXXElSjp1HnGOhhcwyOEFg7XcbnhvU2QwQ70UBP8v8rv6HWZ2SYL99JRksjNpq2x-F0Vw5CBAxL1c9GrtchREUhxK8wRpDzNEhQ-9WuuGy2NLPdXEME2Cg50Ki2thf1733RBG-WGZzARnIgT02E_Qfw'
headers = {
    'Authorization': "Bearer " + token,
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}
print("\n")
print(headers)
print("\n")

queryFilter='userName sw "sec.test"'
urlEncodedFilter = parse.quote(queryFilter)
print(urlEncodedFilter + "\n")

conn.request("GET", "/admin/v1/Users?startIndex=1001&count=2000&filter=" + urlEncodedFilter,None,headers)

res = conn.getresponse()
data = res.read()
print(res.code)
decodedData = data.decode("utf-8")

print("\n")
print(decodedData)

# parse token
token = []
def as_token(dct):
    if 'id' in dct:
        print(dct['id'])
        token.append(dct['id'])
    return dct

json.loads(decodedData, object_hook=as_token)

with open('list1','w') as file:
    for id in token:
        file.write(id)
        file.write('\n')

# get access file by ftp
ftp = FTP('slc04ktl.us.oracle.com','yangzhao', 'i57734G77')

ftp.cwd('/scratch/yangzhao/')
#ftp.retrlines('list')
ftp.storlines('STOR list_1', open('list1','br'))
