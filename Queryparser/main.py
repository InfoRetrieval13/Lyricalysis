import json
from util import translator

#simulate incoming json from searchUI
f = open('sample_search.json')
query = json.load(f)


query_string = ''

#iterate through the json object
for i in range(0, len(query)):
	condition = query[i]
	field = condition['type']
	negation = condition['start']
	connector = condition['end']

	translator