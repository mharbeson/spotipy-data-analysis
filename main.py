import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
import pandas as pd
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environmental variables from .env file
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# Get the username from terminal
# username = sys.argv[1]
username = '1236194609'
scope = 'user-read-private user-read-playback-state user-library-read user-read-recently-played'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# Show recently played
# recently_played = spotifyObject.current_user_recently_played(limit=1)

# # Write Recently Played Dict to JSON file
# with open("data/song.json", "w") as f:
#     json.dump(recently_played,f)



# Retrieve track identifiers from song
def getTrackFeatures(id):
    track_info = spotifyObject.track(id)
    features = spotifyObject.audio_features(id)
    print(features)

    danceability = features[0]['danceability']
    energy = features[0]['energy']
    key = features[0]['key']
    loudness = features[0]['loudness']
    mode = features[0]['mode']
    speechiness = features[0]['speechiness']
    acousticness = features[0]['acousticness']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    valence = features[0]['valence']
    tempo = features[0]['tempo']
    track_type = features[0]['type']

    # for loop to pull json elements and convert to dict
    # for track in features:
    #     track_characteristics = []
    #     for characteristic in track:
    #         track_characteristics[characteristic].append()
    track = [danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,track_type]
    return track

def getTrackId():
    id = []
    recently_played = spotifyObject.current_user_recently_played(limit=1)
    for key, value in recently_played['items'][0]['track'].items():
        # print(value)
        # track = key['track']
        # id.append(key['id'])
        print(key, value)
    return id

# with open("data/characteristics.json", "a") as f:
#     for item in recently_played[]
#     json.dump(recently_played,f)


# Test function
# test = '3jK9MiCrA42lLAdMGUZpwa'
# print(getTrackFeatures(test))

# print(recently_played)

print(getTrackId())

# Use pandas or numpy to graph