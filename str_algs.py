line="hello, world"

def f_change(line):
	print(line)
	out=line[::-1]
	return print(out)

f_change(line)
