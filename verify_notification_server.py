from ftplib import FTP
import http.client
from urllib import parse
import ssl
import json

dockerEnvHost = 'hostname'
dockerEnvPort = 8943
queryFilter = '(data co "test_reset@myservice.invalid")'

t = []
# define call back function
def print_line(line):
    t.append(line)

# get access file by ftp
ftp = FTP('host.us.oracle.com','username', 'password')

ftp.cwd('/dir/path/in/ftp/server')
ftp.retrlines('list')

# read access token
ftp.retrlines('RETR admin.accessToken',callback=print_line)
print('got access token')
accessToken = ''.join(t)
print(accessToken)

# close connection
ftp.quit()

# rest request
conn= http.client.HTTPSConnection(dockerEnvHost,dockerEnvPort,context=ssl._create_unverified_context())
conn.set_debuglevel(1)
headers = {
    'Authorization': "Bearer " + accessToken,
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}
print("\n")
print(headers)
print("\n")

urlEncodedFilter = parse.quote(queryFilter)
print(urlEncodedFilter + "\n")
conn.request("GET", "/admin/v1/UserTokens?filter=" + urlEncodedFilter,None,headers)

res = conn.getresponse()
data = res.read()
print(res.code)
decodedData = data.decode("utf-8")

print("\n")
print(decodedData)

# parse token
token = []
def as_token(dct):
    if 'token' in dct:
        print(dct['token'])
        token.append(dct['token'])
    return dct

json.loads(decodedData, object_hook=as_token)

# encode url
encodedToken = parse.quote(token[0])

# combine url
url = 'https://' + dockerEnvHost + ':' + str(dockerEnvPort) + '/ui/v1/resetpwd?token=' + encodedToken;
print("\n")
print(url)