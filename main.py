import os
import sys
import spotipy
import spotipy.util as util
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from json.decoder import JSONDecodeError
from dotenv import load_dotenv

# Load environmental variables from .env file
load_dotenv(".env")

# Get the username from terminal
try: 
    username = sys.argv[1]
except:
    print('No username arg passed, using static username')
    username = '1236194609'

scope = 'user-read-private user-read-playback-state user-library-read user-read-recently-played'

def get_key_env(key_name):
    """returns the value of the key - from OS env file"""
    key_value = os.getenv(key_name)
    return key_value

SPOTIPY_CLIENT_ID = get_key_env('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = get_key_env('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = get_key_env('SPOTIPY_REDIRECT_URI')

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)


''' Returns the ID number of a track'''
def getTrackId(saved_songs):
    for item in saved_songs['items']:
        track = item['track']
        id = track['id']
    return id


''' Return total number of songs in users saved tracks '''
def getUserSavedSongsTotal():
    tempSong = spotifyObject.current_user_saved_tracks(limit=1)
    return tempSong['total']


''' Returns list of current users liked songs. Currently rate limited to the last 500 tracks liked. See comment below. '''
def getCurrentUserSavedSongs():
    savedSongs = []
    increment = 1
    offset = 0

    #######################################################################################################################
    # Limit calls to 500 to prevent Application from being blocklisted. This can be commented out to fully use application.
    # totalSongs = getUserSavedSongsTotal()
    # if totalSongs > 500:
    #     totalSongs = 500
    #######################################################################################################################

    totalSongs = 20
    while offset < totalSongs:
        temp = spotifyObject.current_user_saved_tracks(limit=increment, offset = offset)
        ids = getTrackId(temp)
        savedSongs.append(ids)
        offset += increment
        print(f"Pulling track {offset} of {totalSongs}")
    return savedSongs


''' Returns list of track features '''
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

''' Requests data from Spotify and returns list of tracks with features '''
def trackFeaturesGenerator():
        tracks = []
        recent_songs = getCurrentUserSavedSongs()
        for item in recent_songs:
            print(f'Anlyzing track {recent_songs.index(item) + 1} of {len(recent_songs)}')
            track = getTrackFeatures(item)
            tracks.append(track)
        return tracks
    

''' Generates CSV using Pandas dataframes'''
def spotifyCSV(tracks):
    df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])
    df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d')
    df.to_csv('data/spotipy.csv', sep = ',')


''' Prune Data from CSV for analysis '''
def pruneData(csvName):
    df = pd.read_csv(csvName)
    df.columns = ['index', 'name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    df = df.drop(columns=['index', 'name', 'album', 'artist', 'release_date', 'length', 'popularity'])
    dataCorrelation = df.corr()
    return df, dataCorrelation

''' Generate seaborn heatmap '''
def heatmap(dataCorrelation):
    # Generate mask to remove duplicates in heatmap
    mask = np.triu(np.ones_like(dataCorrelation, dtype=bool))
    # Configure size of graph
    f, ax = plt.subplots(figsize=(12, 12))
    # Generate colormap
    # cmap = sn.diverging_palette(230, 20, as_cmap=True)
    cmap = sn.diverging_palette(150, 275, s=80, l=55, n=9)

    # sn.heatmap(dataCorrelation, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)
    sn.heatmap(dataCorrelation, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)
    plt.show()


''' Main function to run program '''
def main():
    try:
        tracks = trackFeaturesGenerator()
        spotifyCSV(tracks)
        df, dataCorrelation = pruneData('data/spotipy.csv')
        print(df.describe())
        heatmap(dataCorrelation)


    except: 
        print('Unknown Error, Please restart')


if __name__ == '__main__':
    main()