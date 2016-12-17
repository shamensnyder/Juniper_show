from netmiko import ConnectHandler
from datetime import datetime
import getpass
import time
import sys
import re
import os

print('CTRL-C to Exit Program at any time.')

def enterPassword():
  while True: # repeat forever
    password = getpass.getpass('Enter password:')
    password_again = getpass.getpass('Confirm password:')
    if password != password_again:
      print ('Passwords do not match. Please try again.')
    else:
      return password

def getDevices():
  while True:
    host_file_or_ip_address = input('Do you want to use a host file?(Enter yes or no):')
    if host_file_or_ip_address == 'yes':
      file_path = input('Enter file path for host_file: ')
      with open(file_path,'r') as f1: # Opens file in read mode
        devices = f1.read().splitlines() # Creates list removes \n
        f1.close()
      return devices
    elif host_file_or_ip_address == 'no':
      devices = []
      i = 0
      while 1:
        i += 1
        device = input('Enter IP Addresses (Press Enter to stop):')
        if device == '':
          break
        devices.append(device)
        devices = [x.strip(' ') for x in devices]
        print(devices)
        return devices
    else:
        print('Enter yes or no:')

username = input('Enter username for device login:')

password = enterPassword()

devices = getDevices()

run_command = input('Type command you would like to run:')
command_not_allowed = re.match(r'\brequest\b|\brestart\b|\bstart\b', run_command) #Regular Expression
if command_not_allowed:
    print('That command is not allowed. Exiting script')
    sys.exit()

device_type = 'juniper'

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

