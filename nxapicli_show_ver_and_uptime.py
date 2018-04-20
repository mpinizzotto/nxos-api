

import requests
import json

"""
Modify these please
"""

file = open('nexus_ips.txt','r')

for line in file:

    device_ip_list = line.strip().split(',')

    device_info = {}
    device_info['ip'] = device_ip_list[0]
    device_info['username'] = device_ip_list[1]
    device_info['password'] = device_ip_list[2]
    
    url = "http://" + device_info['ip'] + '/ins' 
    switchuser = device_info['username']
    switchpassword = device_info['password']

	
    print ''
    print '-----------------------------------------------'
    print 'Logging into ' + device_info['ip'] + ' with username ' + device_info['username']
	
    myheaders={'content-type':'application/json'}
    
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show version",
        "output_format": "json"
      }
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, verify=False, auth=(switchuser,switchpassword)).json()
    
    print 'Hostname: ',response['ins_api']['outputs']['output']['body']['host_name']
    print 'Uptime in days: ',response['ins_api']['outputs']['output']['body']['kern_uptm_days'] 
    print ''
  
	
    

   