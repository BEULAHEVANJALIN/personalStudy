def get_keys(json_obj):
	keys = []
	if type(json_obj) == dict:
		keys = list(json_obj.keys())
		for k in json_obj:
			keys += get_keys(json_obj[k])
	elif type(json_obj) == list:
		for v in json_obj:
			keys += get_keys(v)
	d = {}
	for key in keys:
		d[key] = None
	return d

d = get_keys(d)

