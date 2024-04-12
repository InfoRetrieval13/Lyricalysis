def operator_conversion(op_to_convert, mag):
	if op_to_convert == 'MoreThan/Equals' or op_to_convert == 'LongerThan/Equals' or op_to_convert == 'LaterThan/Equals':
		return '[' + str(mag) + ' TO *]'

	if op_to_convert == 'LessThan/Equals' or op_to_convert == 'ShorterThan/Equals' or op_to_convert == 'EarlierThan/Equals':
		return '[* TO ' + str(mag) + ']'

def date_conversion(month, year):
	month_to_number = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
	}
	return year + '-' + month_to_number[month] + '-01T00:00:00Z'


def translator(field_query):

	if field_query[1] == 'artists' or field_query[1] == 'genres' or field_query[1] == 'emotions':
		field = field_query[1][:-1]
		string = ''
		for data in field_query[2]:
			if data == 'OR':
				string = string + 'OR'

			elif data == 'AND':
				string = string + 'AND'

			else:
				string = string + field + ':' + data

			string = string + ' '
	


	elif field_query[1] == 'intensity' or field_query[1] == 'duration' or field_query[1] == 'date':
		field = field_query[1]
		string = ''
		for data in field_query[2]:
			if data == 'OR':
				string = string + 'OR'

			elif data == 'AND':
				string = string + 'AND'

			else:
				data = data.split(' ')
				if field == 'intensity': 
					magnitude = data[-1]
					data = data[:-1]

				elif field == 'duration': 
					magnitude = data[-2]
					data = data[:-2]

				else: 
					field = 'release_date'
					month_date = data[-2:]
					magnitude = date_conversion(month_date[0], month_date[1])
					data = data[:-2]

				#print(''.join(data), magnitude)

				string = operator_conversion(''.join(data), magnitude)

			string = field + ':' + string + ' '


	elif field_query[1] == 'explicit': 
		field = field_query[1]
		data = field_query[2]

		if data == 'yes': return ''
		elif data == 'no': data = 'false'
		elif data == 'only': data = 'true'

		string = 'AND ' + field + ':' + data

	string = string.strip()
	string = '(' + string + ')'


	if field_query[0] == 'NOT':
		string = 'NOT' + string

	if field_query[3]:
		string = string + ' ' + field_query[3] + ' '

	return string