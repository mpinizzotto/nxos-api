# Config interface using ncclient

!/usr/bin/env python

from ncclient import manager

switch = '172.16.30.24'
username = 'admin'
password = 'P@ssword'

if __name__ == '__main__':

    with manager.connect(host='nxosv', port=22, username=username, password=password,
                         hostkey_verify=False, device_params={'name': switch},
                         allow_agent=False, look_for_keys=False) as device:

        commands = ['config t', 'interface Ethernet2/6', 'switchport', 'description Configured by Python ncclient']
        nc_config_reply = device.exec_command(commands)
        print nc_config_reply.xml
		