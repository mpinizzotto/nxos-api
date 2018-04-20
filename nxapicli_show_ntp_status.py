# Prints NTP peer-status information
# uses nxapi cli_show
#######################################


import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

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
            "input": "show ntp peer-status",
            "output_format": "json"
        }
    }
    url = 'http://172.16.30.24/ins'

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    rx_object = json.loads(response.text)
    data = rx_object['ins_api']['outputs']['output']['body']['TABLE_peersstatus']['ROW_peersstatus']
    
    print ""
    print "------------------------------"
	
    for item in data:
        
        if item['syncmode'] == '*':
            print "NTP server ", item['remote'], "is selected for sync"
        elif item['syncmode'] == '=':
            print "NTP server ", item['remote'], "is polled for client mode"
        else:
            continue
			
    print ""
		
  
	
	
	
	