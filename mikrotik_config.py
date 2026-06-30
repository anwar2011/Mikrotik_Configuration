import paramiko
import netmiko
from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()


for devices in devices_list:
    try:
        print ('Connecting to device" ' + devices)
        ip_address_of_device = devices
        device = {
            'device_type': 'mikrotik_routeros',
            'ip': ip_address_of_device,
            'username': 'bras',
            'password': 'OmlamP2024||'
        }

        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(commands_list)
        print (output)
        print("Successful!")
    except:
        print("failed")
        with open("failed_device.txt", "a+") as fail_dev:
            fail_dev.write(ip_address_of_device + '\n')
        continue

