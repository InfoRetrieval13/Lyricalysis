import json
from util import translator
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def query_parser():
	query = request.get_json()

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
		
	endpoint = f"http://localhost:8983/solr/lyrics-dev/select?q={full_query}"

	data = requests.get(endpoint).json()
	docs = json.dumps(data['response']['docs'])

	return docs

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

