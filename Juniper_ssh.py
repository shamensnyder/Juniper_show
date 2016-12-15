from netmiko import ConnectHandler
from datetime import datetime
import getpass
import time
import sys

print('CTRL-C to Exit Program at any time.')
time.sleep(1)

username = input('Enter username for device login:')

def enterPassword():
  while True: # repeat forever
    password = getpass.getpass('Enter password:')
    password_again = getpass.getpass('Confirm password:')
    if password != password_again:
      print ('Passwords do not match. Please try again.')
    else:
      return password
password = enterPassword()

run_command = input('Type command you would like to run:')
if run_command == 'request':
    print('Request commands are not allowed. Exiting script')
    sys.exit()
elif run_command == 'start':
    print('Start commands are not allowed. Exiting script')
    sys.exit()
elif run_command == 'edit':
    print('Edit commands are not allowed. Exiting script')
    sys.exit()
elif run_command == 'restart':
    print('Restart commands are not allowed. Exiting script')
    sys.exit()

device_type = 'juniper'

devices = ['mpr0-wrrnoh', 'mpr0-mrcrpa', 'as0-wrrnoh']

start_time = datetime.now()

for device in devices:
    net_connect = ConnectHandler(device_type = device_type, ip = device, username = username, password = password)
    output = net_connect.send_command(run_command)
    print("***", device, "***")
    print(output)
    print("*** END ***")

end_time = datetime.now()
total_time = end_time - start_time
print ('Total time to run script: ', total_time)
