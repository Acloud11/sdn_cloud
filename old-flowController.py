import requests, json, time

def add_flow(matrix):
    data = {
	"dpid": 1,
	"match":{
	    #"in_port":1
		},
	"instructions": [
	    {
		"type": "APPLY_ACTIONS",
		"len": 24,
		"actions": [
		    {
		        "max_len": 0,
		        "type": "OUTPUT",
		#        "port": 2,
		        "len": 16
		    }
		]
	    }
	]
    }
	#i:in_port; j:out_port
    for i,low in enumerate(matrix):
	for j,tag in enumerate(low):
	    if tag == 1:
		data['match']['in_port'] = i +1
		data['instructions'][0]['actions'][0]['port'] = j+1 
		#print(data)
	        data_json = json.dumps(data)
		print(data)
	        url = 'http://0.0.0.0:8080/stats/flowentry/add'
		#url = 'http://10.10.10.10:8080/stats/flowentry/add'
		try:
	            requests.post(url, data=data_json)
		    time.sleep(2)
		except Exception as e:
		    print(e)
def del_all_flow():
    url = 'http://0.0.0.0:8080/stats/flowentry/clear/'
    try:
	requests.delete(url)
	time.sleep(2)
    except Exception as e:
	print(e)

if __name__ == '__main__':
    matrix = [[0,1],[1,0]]
    #del_all_flow()
    add_flow(matrix)


