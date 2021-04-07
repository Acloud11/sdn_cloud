import requests, json, time

def add_flow(tuples, pid):
    data = {
	"match":{
	    #"in_port":1
		},
#	"instructions": [
#	    {
#		"type": "APPLY_ACTIONS",
#		"len": 24,
		"actions": [
		    {
		        "max_len": 0,
		        "type": "OUTPUT",
		#        "port": 2,
		        "len": 16
		    }
		]
#	    }
#	]
    }
	#i:in_port; j:out_port
    data['dpid'] = pid
    for in_port, out_port in tuples:
	for i in range(2):
	    data['match']['in_port'] = in_port
	    data['actions'][0]['port'] = out_port 
	    #print(data)
	    data_json = json.dumps(data)
	    print(data)
	    url = 'http://localhost:8080/stats/flowentry/add'
	    #url = 'http://10.10.10.10:8080/stats/flowentry/add'
	    try:
	        requests.post(url, data=data_json)
		time.sleep(2)
	    except Exception as e:
		print(e)
def del_all_flow():
    url = 'http://localhost:8080/stats/flowentry/clear/'
    try:
	requests.delete(url)
	time.sleep(2)
    except Exception as e:
	print(e)

if __name__ == '__main__':
    #实际交换机的接口也不会是1、2那么简单，需要更换为实际交换机接口代码
    tuples = [(1,2)]
    #获取实际交换机的pid
    response=response.get('http://localhost:8080/stats/switches')
    pid=response.json()[0]
    #del_all_flow()
    add_flow(tuples, pid)


