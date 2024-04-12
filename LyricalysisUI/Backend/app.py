from flask import Flask
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
    for element in genre.split(","):
        cleaned_genres.append(element.strip())
emotions = list(df['emotion'].unique())
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

if __name__ == '__main__':
    app.run(debug=True)
