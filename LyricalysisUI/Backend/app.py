from flask import Flask, request
import json
from util import translator
from flask_login import LoginManager
from flask_cors import CORS
import pandas as pd
import httpx

app = Flask(__name__)
login_manager = LoginManager(app)

df = pd.read_csv("final_labeled_dataset.csv")
artists = list(df['artist'].unique())
artists.sort()
genres = list(df['genre'].unique())
cleaned_genres = []
for genre in genres:
    genre = eval(genre)
    for subgenre in genre:
        cleaned_genres.append(subgenre.strip())
        
cleaned_genres = list(set(cleaned_genres))
cleaned_genres.sort()
cleaned_genres = [genre.capitalize() for genre in cleaned_genres]

emotions = list(df['emotion'].unique())
emotions.sort()
emotions = [emotion.capitalize() for emotion in emotions]
intensity = list(df['intensity'].unique())

CORS(app)

@app.route('/', methods=['GET'])
def index():
    return {'message': 'Welcome to Lyricalysis API!'}

@app.route('/artists', methods=['GET'])
def get_artists():
    return {'artists': artists}

@app.route('/genres', methods=['GET'])
def get_genres():
    return {'genres': cleaned_genres}

@app.route('/emotions', methods=['GET'])
def get_emotions():
    return {'emotions': emotions}

@app.route('/intensity', methods=['GET'])
def get_intensity():
    return {'intensity': intensity}

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    if data is None:
        return {"error": "Invalid JSON data"}, 400
    print(data)
    return {'data': data}

@app.route('/send_search', methods=['POST'])
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
        
    print("querying:", full_query)
    # endpoint = f"http://localhost:8983/solr/mycore/select?q={full_query}"
    endpoint = f"http://solr:8983/solr/mycore/select?q={full_query}"
    response = httpx.get(endpoint)
    try:
        data = response.json()
        docs = data['response']['docs']
    except:
        return {"docs": [{
                        "album": ["No Results Found"],
                        "track": ["No Results Found"],
                        "track_id": ["7zD97mcPo9fng0aJqUhFvd"],
                        "lyrics": [
                            "No Results Found"
                        ],
                        "duration": [0],
                        "genre": ["NIL"],
                        "release_date": ["2024-01-01T00:00:00Z"],
                        "explicit": [False],
                        "artists": ["NIL"],
                        "url": ["https://open.spotify.com/track/7zD97mcPo9fng0aJqUhFvd"],
                        "name": ["NIL"],
                        "preview_url": ["https://p.scdn.co/mp3-preview/549be7417c775d68366fe86a52f2362d1d35f06f?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        "image": ["https://as1.ftcdn.net/v2/jpg/05/57/94/52/1000_F_557945208_ee1VFo8QxNFOJzZEjbR1gq52lOr1bUwZ.jpg"],
                        "emotion": ["ecstasy"],
                        "intensity": ["3"],
                        "id": "9d298669-e6f6-452a-b324-22d6fc481930",
                        "_version_": 1796230700896092163,
                    }]}
    return {'docs': docs}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
