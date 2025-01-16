from prefect import flow
from requests import get

@flow(log_prints=True)
def print_ip():
  ip = get('https://api.ipify.org').content.decode('utf8')
  print('My public IP address is: {}'.format(ip))
