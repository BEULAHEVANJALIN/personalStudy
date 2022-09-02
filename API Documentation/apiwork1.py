def remove(dic):
	for key in dic:
		if type(dic[key]) == str: 
			dic[key] = 'string'
		if type(dic[key]) == int:
			dic[key] = 0
	return dic

def forlist(l):
	if len(l) != 1:
		l = l[0:1]
	if type(l[0]) == list:
		l[0] = forlist(l[0])
	elif type(l[0]) == str: 
		l[0] = 'string'
	elif type(l[0]) == int:
		l[0] = 0
	elif type(l[0]) == dict:
		l[0] = fordic(l[0])
	return l

def fordic(d): 
	for i in d:
		if i == 'statusCode':
			continue
		if type(d[i]) == list:
			d[i] = forlist(d[i])
		elif type(d[i]) == dict:
			d[i] = fordic(d[i])
		elif type(d[i]) == str: 
			d[i] = 'string'
		elif type(d[i]) == int:
			d[i] = 0
	return d

fordic(d)
