import requests, json, time

def add_flow(tuples, pid):
    data = {
	"match":{
	    #"in_port":1
		},
	"actions": [
	    {
	        "type": "OUTPUT"
	#        "port": 2,
	    }
	]
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
		#time.sleep(2)
	    except Exception as e:
		print(e)
	    demo = in_port
	    in_port = out_port
 	    out_port = demo

def del_all_flow():
    url = 'http://localhost:8080/stats/flowentry/clear/'
    try:
	requests.delete(url)
	#time.sleep(2)
    except Exception as e:
	print(e)

if __name__ == '__main__':
    #
    tuples = [(1,6)]
    #
    response=requests.get('http://localhost:8080/stats/switches')
    print(response.json())
    pid=response.json()[0]
    #del_all_flow()
    add_flow(tuples, pid)


