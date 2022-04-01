import os
import spotipy
import spotipy.util as util
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib as mpl
import matplotlib.pyplot as plt
from os.path import exists
from json.decoder import JSONDecodeError
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


def get_key_env(key_name):
    '''Returns the value of the key - from OS env file'''
    key_value = os.getenv(key_name)
    return key_value


def spotipyCredentials(username, scope):
    ''' Returns token for auth '''
    try:
        token = util.prompt_for_user_token(username, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)
    return token


def getTrackId(saved_songs):
    ''' Returns the ID number of a track'''
    for item in saved_songs['items']:
        track = item['track']
        id = track['id']
    return id


def getUserSavedSongsTotal():
    ''' Return total number of songs in users saved tracks '''
    tempSong = spotifyObject.current_user_saved_tracks(limit=1)
    return tempSong['total']


def getCurrentUserSavedSongs():
    ''' Returns list of current users liked songs. Currently rate limited to the last 500 tracks liked. See comment below. '''
    savedSongs = []
    increment = 1
    offset = 0

    #######################################################################################################################
    # Limit calls to 500 to prevent Application from being blocklisted. This can be commented out to fully use application.
    totalSongs = getUserSavedSongsTotal()
    if totalSongs > 500:
        totalSongs = 500
    #######################################################################################################################

    while offset < totalSongs:
        temp = spotifyObject.current_user_saved_tracks(limit=increment, offset = offset)
        ids = getTrackId(temp)
        savedSongs.append(ids)
        offset += increment
        print(f"Pulling track {offset} of {totalSongs}")
    return savedSongs


def getTrackFeatures(id):
    ''' Returns list of track features '''
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

    # Assign values to list
    track_features = [name, album, artist, release_date, length, popularity, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo]
    return track_features


def trackFeaturesGenerator():
    ''' Requests data from Spotify and returns list of tracks with features '''
    tracks = []
    recent_songs = getCurrentUserSavedSongs()
    for item in recent_songs:
        print(f'Anlyzing track {recent_songs.index(item) + 1} of {len(recent_songs)}')
        track = getTrackFeatures(item)
        tracks.append(track)
    return tracks
    

def spotifyCSV(tracks):
    ''' Generates CSV using Pandas dataframes'''
    df = pd.DataFrame(tracks, columns = ['Name', 'Album', 'Artist', 'Release_Date', 'Length', 'Popularity', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo'])
    df['Release_Date'] = pd.to_datetime(df['Release_Date'], format='%Y-%m-%d')
    df.to_csv(f'data/spotipy-{username}.csv', sep = ',')


def pruneData(csvName):
    ''' Prune Data from CSV for analysis '''
    df = pd.read_csv(csvName)
    df.columns = ['Index', 'Name', 'Album', 'Artist', 'Release_Date', 'Length', 'Popularity', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']

    # Drop artist,album,track name, etc
    featuresDF = df.drop(columns=['Index', 'Name', 'Album', 'Artist', 'Release_Date', 'Length', 'Popularity', 'Mode', 'Key'])
    featuresDataCorrelation = featuresDF.corr()

    # Drop unused song features
    trackDF = df.drop(columns=['Length', 'Popularity', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo'])

    return trackDF, featuresDF, featuresDataCorrelation


def trackFeatureHeatmap(featuresDataCorrelation):
    ''' Generate Track Feature heatmap '''

    # Generate mask to remove duplicates in heatmap
    mask = np.triu(np.ones_like(featuresDataCorrelation, dtype=bool))
    # Configure size of graph
    f, ax = plt.subplots(figsize=(12, 12))
    # Generate colormap
    cmap = sn.diverging_palette(150, 275, s=80, l=55, n=9)
    # Generate heatmap to screen
    sn.heatmap(featuresDataCorrelation, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)
    plt.show()


def releaseYearHistogram(trackDF):
    ''' Generate Histogram based on Release Year '''
    yearDF = trackDF[['Release_Date']]
    yearDF['Release Year'] = pd.to_datetime(yearDF['Release_Date']).dt.year
    f, ax = plt.subplots(figsize=(12, 12))
    sn.despine(f)
    # Build histogram
    sn.histplot(data=yearDF, x='Release Year', binwidth=2, color='green', alpha=0.5)
    # Modify X axis
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    ax.set_xticks([1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])
    # Generate histogram to screen
    plt.show()


def usernamePrompt():
    ''' Returns username to be used '''
    username = input('Enter username to run analysis on:\n')
    return username

def getUsername():
    ''' Returns username / ID '''
    user = spotifyObject.current_user()
    username = user['id']
    displayname = user['display_name']
    return username, displayname

def continuePrompt():
    ''' Determines if User would like to re-run program '''
    continueVar = input('Analysis complete. Rerun? (Y/N)\n(Y): Yes\n(N): No\nSelection: ').lower()
    if continueVar == 'y':
        main()
    elif continueVar == 'n':
        print('Goodbye')
        exit()
    else:
        print('Invalid response')
        continuePrompt()


def processCSV(csvFileName):
    ''' Processes CSV for Data Analysis'''
    trackDF, featuresDF, featuresDataCorrelation = pruneData(csvFileName)
    print('Basic info on Tracks\n')
    print(trackDF.describe())
    print('Track Feature Correlation Table Information')
    print(featuresDF.describe())
    input('Press any key to continue.\n')
    print('Close Graph to continue.\n')
    releaseYearHistogram(trackDF)
    print('Close Graph to continue.\n')
    trackFeatureHeatmap(featuresDataCorrelation)
    continuePrompt()


def main():
    ''' Main function to run program '''
    dataPrompt = input('Select an option for analysis:\n(1) Use the sample dataset\n(2) Generate new data\nSelection: ')
    if dataPrompt == '1':
        processCSV('data/spotipy-complete.csv')
    elif dataPrompt == '2':
        # Check for existing user dataset
        file_exists = exists(f'data/spotipy-{username}.csv')
        if file_exists == True:
            if username == 'complete':
                processCSV(f'data/spotipy-{username}.csv')
            file = input('Spotify CSV exists, would you like to process existing data? (Y/N)\n(Y): Yes\n(N): No\nSelection: ').lower()
            if file == 'y':
                pass
            elif file == 'n':
                tracks = trackFeaturesGenerator()
                spotifyCSV(tracks)
            else:
                print('Invalid User Prompt')

            # Process Existing CSV
            processCSV(f'data/spotipy-{username}.csv')

        # If file does not exist, regenerate CSV and process
        else:
            tracks = trackFeaturesGenerator()
            spotifyCSV(tracks)
            processCSV(f'data/spotipy-{username}.csv')


if __name__ == '__main__':
    try:
        # Load environmental variables
        load_dotenv(".env")

        # Spotify secret keys
        SPOTIPY_CLIENT_ID = get_key_env('SPOTIPY_CLIENT_ID')
        SPOTIPY_CLIENT_SECRET = get_key_env('SPOTIPY_CLIENT_SECRET')
        SPOTIPY_REDIRECT_URI = get_key_env('SPOTIPY_REDIRECT_URI')
    except:
        print('Missing ENV file. Please review readme')

    # Create spotipy object
    try:
        scope = 'user-read-private user-read-playback-state user-library-read user-read-recently-played'
        clientAuthManager = SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri = SPOTIPY_REDIRECT_URI, scope=scope)
        spotifyObject = spotipy.Spotify(auth_manager=clientAuthManager)
        username, displayname = getUsername()
    except:
        print('User is not whitelisted. Contact developer to be added\n')
        # If user is not whitelisted, use test dataset
        print('Using test dataset from validated user\nGenerating new data will just use test dataset\n')
        username = 'complete'
        
    # Execute main function
    main()
