from netmiko import ConnectHandler
from datetime import datetime
import getpass
import time
import sys
import re
import os

print('CTRL-C to Exit Program at any time.')
time.sleep(1)

while True:
    host_file_or_ip_address = input('Do you want to use a host file?(Enter yes or no):')
    if host_file_or_ip_address == 'yes':
        file_path = input('Enter file path for host_file: ')
        # Opens file in read mode
        f1 = open(file_path,'r')
        # Creates list
        devices = f1.readlines()
        print(devices)
    elif host_file_or_ip_address == 'no':
        devices = input('Enter IP Addresses:')
        print(devices)
    else:
        print('Enter yes or no:')

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
command_not_allowed = re.match(r'\brequest\b|\brestart\b|\bstart\b', run_command) #Regular Expression
if command_not_allowed:
    print('That command is not allowed. Exiting script')
    sys.exit()

device_type = 'juniper'

#devices = ['172.30.0.248', '172.30.0.246'] #IP or FQDN
start_time = datetime.now()
for device in devices:
    net_connect = ConnectHandler(device_type = device_type, ip = device, username = username, password = password)
    output = net_connect.send_command(run_command)
    print("***", device, "***")
    print(output)
    print("*** END ***\n")

end_time = datetime.now()
total_time = end_time - start_time
print ('Total time to run script: ', total_time)
