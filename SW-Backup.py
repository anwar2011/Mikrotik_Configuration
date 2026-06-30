from netmiko import cisco_base_connection
import getpass
user = input("anwar.hossain ")
password = getpass.getpass("Password: ")

backup_folder = 'C:/network_backups'
switch_list = [
    '192.168.1.10',     # কোর সুইচ
    '192.168.1.20',     # ডিস্ট্রিবিউশন সুইচ
    '192.168.1.30'      # এক্সেস সুইচ
]
