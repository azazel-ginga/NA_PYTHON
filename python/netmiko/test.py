from netmiko import ConnectHandler
shenzhou = {'device_type':'shenzhou_ios',    'ip':'192.168.1.254',    'username':'user1',    'password': '123456',    'secret':'123456'}
connect=ConnectHandler(**shenzhou)
connect.enable()

out_put_2 = connect.send_config_set('int vlan 20') 
show_route = connect.send_command('show ip route')
