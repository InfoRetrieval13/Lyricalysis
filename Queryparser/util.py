def translator(field, data):
	
	if field == 'duration':
		return field + "[" + str(data[0]) + "TO" + str(data[1]) + "]"

	if field == 