
    
import requests
import json
requests.packages.urllib3.disable_warnings()


file = open('nexus_ips.txt','r')

for line in file:

    device_ip_list = line.strip().split(',')

    device_info = {}
    device_info['ip'] = device_ip_list[0]
    device_info['username'] = device_ip_list[1]
    device_info['password'] = device_ip_list[2]
    
    url = "https://" + device_info['ip'] + '/ins' 
    switchuser = device_info['username']
    switchpassword = device_info['password']

	
    print ''
    print '-----------------------------------------------'
    print 'Logging into ' + device_info['ip'] + ' with username ' + device_info['username']
    print ''
    print ''
    print ''
	
    myheaders={'content-type':'application/json'}
    
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show interface",
        "output_format": "json"
      }
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, verify=False, auth=(switchuser,switchpassword)).json()
    #interface_list = []
    
  	
    print 'Interface          CRC Error    Input Error          '
    print '---------------    ----------   -----------'
	
    for dct in response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']:
        try:
		    if (dct['interface']) != 'mgmt0' and (dct['state']) == 'up':
			    print '{0:22} {1:12} {2:9}'.format((dct['interface']),(dct['eth_crc']),(dct['eth_inerr']))
        except (ValueError, KeyError):                                         
            pass
	continue	   
	
    

   