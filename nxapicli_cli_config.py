#!/usr/bin/env python

# Uses NX-API CLI to list of commands to device
# returns HTTP 200 on success


import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {
        'Content-Type': 'application/json'
    }

    commands = ['config t', 'vlan 150', 'exit', 'interface Eth2/5', 'switchport', 'switchport access vlan 150']

    commands = ' ; '.join(commands) # takes list of strings and seperates them via semi-colon



    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_conf",
            "chunk": "0",
            "sid": "1",
            "input": commands,
            "output_format": "json"
        }
    }
    url = 'http://nxosv/ins'

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    rx_object = json.loads(response.text)

    print json.dumps(rx_object, indent=4) #if commands are successful should get back http 200