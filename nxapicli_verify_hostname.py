##############################################
#nxapicli 
#unititest command matches expected outcome
#
##############################################

#!/usr/bin/env python

import unittest
import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

#-------------------------------------------------------

class TestHostname(unittest.TestCase):

    @staticmethod
    def get_output(commands):
        auth = HTTPBasicAuth('admin', 'P@ssw0rd')
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": commands,
                "output_format": "json"
            }
        }
        
        url = 'http//<my_ip_address/ins'
        response = requests.post(
		        url, data=json.dumps(payload), headers=headers, auth=auth)
        rx_object = json.loads(response.text)
        return rx_object
 
    def test_hostname(self):
        expected_hostname = 'hostname.local'
        commands = ['show hostname']
        rx_object = self.get_output(commands)
        output = rx_object['ins_api']['outputs']['output']['body']
        hostname = output['hostname']

        self.assertEquals(expected_hostname, hostname)

if __name__ == '__main__':
    unittest.main()
