from netmiko import ConnectHandler,NetmikoAuthenticationException,NetmikoTimeoutException
from getpass import getpass
import ipaddress

#Gathering credentials
username = input('Please enter the username: ')
password = getpass('Please enter the password: ')
secret = getpass('Please enter the secret: ')

#Gathering devices IPs
print('Please enter devices IPs one by one and type "done" when finish.')
ip_list = []
while True:
    ip_add = input('Enter IP: ')
    if ip_add.lower().strip() == 'done':
        break
    try:
        ipaddress.IPv4Address(ip_add)  #Check IP address format
        ip_list.append(ip_add)
    except ipaddress.AddressValueError:
        print('Invalid IP address! Please try again.')

#Gathering VLANs IDs
print('Please enter VLANs IDs one by one and type "done" when finish.')
vlan_id_list = [] 
while True:
    vlan_id = input('Enter ID: ')
    if vlan_id.lower().strip() == 'done':
        break
    if vlan_id.isdigit() and 1 <= int(vlan_id) <= 4094:
        if vlan_id in vlan_id_list:
            print(f'Error: VLAN {vlan_id} is already exists. Please enter a unique VLAN ID.')
        else:
            vlan_id_list.append(vlan_id)
    else:
        print('Error: VLAN ID must be a digit number between 1 and 4094.')

#Gather VLANs names
print('Please enter VLANs names one by one and if no name, press enter and leave it blank then type "done" when finish.')
vlan_names_list = []
while True:
    vlan_name = input('Enter name: ')
    if vlan_name.lower().strip() == 'done':
        break
    if vlan_name:
        vlan_names_list.append(vlan_name)
    else:
        vlan_names_list.append(None)

#Define the function
def config_vlans(username, password, secret, ip_list, vlan_id_list, vlan_names_list):
    for ip in ip_list:
        device = {
                    'device_type' : 'cisco_ios',
                    'username' : username,
                    'host' : ip,
                    'password' : password,
                    'secret' : secret
                 }
        try:
            print(f'Connecting to host {ip}......')
            net_connect = ConnectHandler(**device)
            net_connect.enable()
            for id,name in zip(vlan_id_list,vlan_names_list):
                commands = [f'vlan {id}']
                if name:
                    commands.append(f'name {name}')
                output = net_connect.send_config_set(commands)
                print(output)
                verification = net_connect.send_command('sh vlan br')
                print(verification)
                print(f'VLANs have been configured successfully on host {ip}!')
        except NetmikoAuthenticationException:
            print(f'Error: Authentication failed to host {ip}. Please check the credentials.')
        except NetmikoTimeoutException:  
            print(f'Error: Timeout while connecting to host {ip}. This host might be unreachable.')
        except Exception as e:
            print(f'Unexpected error with host {ip}: {e}.')

config_vlans(username,password,secret,ip_list,vlan_id_list,vlan_names_list)
print('VLANs have been configured on all hosts!')