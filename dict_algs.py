ivan={
	"name":"ivan",
	"age":34,
	"children":[{
		"name":"vasja",
		"age":17,
		},{
			"name":"petja",
			"age":10,
			}],
}
darja={
	"name":"darja",
	"age":41,
	"children":[{
		"name":"kirill",
		"age":21,
		},{
			"name":"pavel",
			"age":25,
			}],
}
emps=[ivan,darja]

def f_child(emps, age_of_child):
	filtered = []
	for worker in emps:
		for children in worker['children']:
		    if children['age'] >= age_of_child:
			    filtered.append(worker['name'])
			    break
	return filtered
	
print(f_child(emps, 18))
