import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials

# Get the username from terminal
# username = sys.argv[1]
username = '1236194609'
scope = 'user-read-private user-read-playback-state user-library-read user-read-recently-played'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope


# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# Get current device
devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']
recently_played = spotifyObject.current_user_recently_played(limit=50)


# Write Recently Played Dict to JSON file
with open("data/song.json", "a") as f:
    json.dump(recently_played,f)

test = '3Z8FwOEN59mRMxDCtb8N0A'

def getTrackFeatures(id):
    meta = spotifyObject.track(id)
    features = spotifyObject.audio_features(id)
    acousticness = features[0]['acousticness']

    track = [acousticness]
    print(features)
    return track

getTrackFeatures(test)