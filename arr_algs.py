massive=[27, 75, 16, 201, 70, 40]

def f_begin(massive): 
	print("massive: ")
	for i in range(len(massive)):
	       print(massive[i])

def f_min(massive):
	print("min of massive:")
	return print(min(massive))

def f_med(massive):
	print ("med of massive:")
	med = sum(massive)/len(massive)
	return print(med)
	
f_begin(massive)
f_min(massive)
f_med(massive)
