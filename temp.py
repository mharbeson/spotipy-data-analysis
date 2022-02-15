# Get current device
devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']