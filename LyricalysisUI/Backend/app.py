from flask import Flask, request
from flask_login import LoginManager
from flask_cors import CORS
import pandas as pd
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

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

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
if __name__ == '__main__':
    app.run(debug=True)
