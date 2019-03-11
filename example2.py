from filestack import security as create_security
from filestack import Client
import time
import os

policy = {
  'expiry': int(time.time()) + 15 * 60,
  'path': '/my-user/',
  'maxSize': 10000000,
  'container': 'user-uploads',
}
store_params = {
    'path': '/my-user/',
    'container': 'user-uploads',
}
print(os.environ.get('FILESTACK_SECRET'))

def gen_credentials(policy, filestack_secret):
  creds = {}
  sec = create_security(policy, os.environ.get('FILESTACK_SECRET'))
  creds['policy'] = sec['policy'].decode('ascii')
  creds['signature'] = sec['signature']
  return(creds)

client = Client("A9UmXdpXcRY2dIPsZsBHfz", security=gen_credentials(policy, os.environ.get('FILESTACK_SECRET')))

new_filelink = client.upload(filepath="./Chart.svg", params=store_params)
print(new_filelink)
