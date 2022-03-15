import os
import sys
import spotipy
import webbrowser
import pandas as pd
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environmental variables from .env file
load_dotenv("/etc/environment")

# Get the username from terminal
# username = sys.argv[1]
username = '1236194609'
scope = 'user-read-private user-read-playback-state user-library-read user-read-recently-played'

def get_key_env(key_name):
    """returns the value of the key - from OS env file"""
    key_value = os.getenv(key_name)
    return key_value

# SPOTIPY_CLIENT_ID = get_key_env('SPOTIPY_CLIENT_ID')
# SPOTIPY_CLIENT_SECRET = get_key_env('SPOTIPY_CLIENT_SECRET')
# SPOTIPY_REDIRECT_URI = get_key_env('SPOTIPY_REDIRECT_URI')

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)


def getTrackId(saved_songs):
    for item in saved_songs['items']:
        track = item['track']
        id = track['id']
    return id


# Return total number of songs in users saved tracks
def getUserSavedSongsTotal():
    tempSong = spotifyObject.current_user_saved_tracks(limit=1)
    return tempSong['total']


def getCurrentUserSavedSongs():
    savedSongs = []
    increment = 1
    # Max increment spotipy supports
    # increment = 20
    offset = 0
    totalSongs = getUserSavedSongsTotal()
    # totalSongs = 20
    while offset < totalSongs:
        temp = spotifyObject.current_user_saved_tracks(limit=increment, offset = offset)
        # print(temp)
        # for item in temp:
        #     ids = getTrackId(temp)
        #     savedSongs.append(ids)
        #     print(ids)
        ids = getTrackId(temp)
        savedSongs.append(ids)
        offset += increment
        print(f"Pulling track {offset} of {totalSongs}")
    return savedSongs


# Retrieve track identifiers from song
def getTrackFeatures(id):
    track_info = spotifyObject.track(id)
    features = spotifyObject.audio_features(id)

    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    release_date = track_info['album']['release_date']
    length = track_info['duration_ms']
    popularity = track_info['popularity']

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


    track_features = [name, album, artist, release_date, length, popularity, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo]
    return track_features



tracks = []
recent_songs = getCurrentUserSavedSongs()
for item in recent_songs:
    print(f'Anlyzing track {recent_songs.index(item) + 1} of {len(recent_songs)}')
    track = getTrackFeatures(item)
    tracks.append(track)


# Use pandas or numpy to graph
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])

df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d')

df.to_csv('data/spotipy.csv', sep = ',')
