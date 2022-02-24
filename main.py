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

def get_key_env(key_name):
    """returns the value of the key - from OS env file -- BEST PRACTICE METHOD """
    key_value = os.getenv(key_name)
    return key_value

# SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
# SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
# SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# SPOTIPY_CLIENT_ID = get_key_env('SPOTIPY_CLIENT_ID')
# SPOTIPY_CLIENT_SECRET = get_key_env('SPOTIPY_CLIENT_SECRET')
# SPOTIPY_REDIRECT_URI = get_key_env('SPOTIPY_REDIRECT_URI')


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

# def getTrackId():
#     id = []
#     recently_played = spotifyObject.current_user_recently_played(limit=50)
#     for item in recently_played['items']:
#         track = item['track']
#         id.append(track['id'])
#     return id

# def getTrackId(saved_songs):
#     id = []
#     # saved_songs = spotifyObject.current_user_saved_tracks(limit=20)
#     # print(saved_songs)
#     for item in saved_songs['items']:
#         track = item['track']
#         id.append(track['id'])
#     return id

def getTrackId():
    id = []
    saved_songs = spotifyObject.current_user_saved_tracks(limit=1)
    print(saved_songs)
    for item in saved_songs['items']:
        track = item['track']
        id.append(track['id'])
    return id

# print(getTrackId())

def get_saved_songs():
    id = []
    songs = {}
    offset = 0
    while offset < 10:
        temp = {}
        temp = (spotifyObject.current_user_saved_tracks(limit=1, offset = offset))
        print(temp)
        songs.update(temp)
        offset += 1
        print(offset)
    # return songs
    # print(songs)
    for item in songs['items']:
        track = item['track']
        id.append(track['id'])
    print(id)
    return id

# Retrieve track identifiers from song
def getTrackFeatures(id):
    track_info = spotifyObject.track(id)
    features = spotifyObject.audio_features(id)
    # print(track_info)
    # print('-' * 150)
    # print(features)

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
    # track_type = features[0]['type']

    # for loop to pull json elements and convert to dict
    # for track in features:
    #     track_characteristics = []
    #     for characteristic in track:
    #         track_characteristics[characteristic].append()
    # meta_info = [name, album, artist, release_date, length, popularity]
    track_features = [name, album, artist, release_date, length, popularity, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo]
    return track_features

# tracks = []
# recent_songs = getTrackId()
# for item in recent_songs:
#     track = getTrackFeatures(item)
#     tracks.append(track)

# df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])
# df.to_csv('data/spotipy.csv', sep = ',')


tracks = []
recent_songs = get_saved_songs()
for item in recent_songs:
    track = getTrackFeatures(item)
    tracks.append(track)

df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])
df.to_csv('data/spotipy.csv', sep = ',')

# Use pandas or numpy to graph