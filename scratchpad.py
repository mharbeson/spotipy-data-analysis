def getTrackId2(user, playlist_id):
    id = []
    play_list = spotifyObject.user_playlist(user, playlist_id)
    # print(play_list)
    for item in play_list['tracks']['items']:
        track = item['track']
        id.append(track['id'])
    return id

# id = getTrackId2('6c4fb1e42dd44f11', '37i9dQZF1DXc8kgYqQLMfH?si=998d66c659194f7a')


