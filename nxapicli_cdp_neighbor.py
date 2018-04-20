#
#NX-API CLI to pull cdp information
#Need to add pulling file from CSV
########################################
    
import requests
import json
requests.packages.urllib3.disable_warnings()

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
        "input": "show cdp neighbor",
        "output_format": "json"
      }
    }
    payload1={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show hostname",
        "output_format": "json"
      }
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, verify=False, auth=(switchuser,switchpassword)).json()
    response1 = requests.post(url, data=json.dumps(payload1), headers=myheaders, verify=False, auth=(switchuser,switchpassword)).json()
	#interface_list = []
	
    
    print 'Hostname: ', response1['ins_api']['outputs']['output']['body']['hostname']
    print ""
    print 'Neighbor Count: ', response['ins_api']['outputs']['output']['body']['neigh_count']
    print 'Local Port       Remote Device                                Remote Port'
    print '--------------   ---------------                              -----------'
    print ""
	
    for dct in response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']:
        print '{0:16} {1:44} {2:9}'.format((dct['intf_id']),(dct['device_id']),(dct['port_id']))
    print ""
      
	
    

   