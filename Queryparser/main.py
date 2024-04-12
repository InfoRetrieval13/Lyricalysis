import json
from util import translator

#simulate incoming json from searchUI
f = open('sample_search.json')
query = json.load(f)

full_query = ''

#iterate through the json object
for i in range(0, len(query)):
	condition = query[i]

	field = condition['type']
	if 'start' in condition: negation = condition['start']
	else: negation = None

	data = condition['data']

	if 'end' in condition: connector = condition['end']
	else: connector = None

	field_query = [negation, field, data, connector]
	string_field_query = translator(field_query)

	full_query += string_field_query
	
print(full_query)



