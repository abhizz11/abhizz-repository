import requests
import base64

# Your Spotify credentials (replace with your actual client_id and client_secret)
CLIENT_ID = 'my id'
CLIENT_SECRET = 'my secret'

# Spotify endpoint for token generation
auth_url = 'https://accounts.spotify.com/api/token'

# Base64 encode the client id and secret
auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Define headers and data for the token request
headers = {
    'Authorization': f'Basic {b64_auth_str}',
}
data = {
    'grant_type': 'client_credentials'
}

# Send POST request to obtain the access token
response = requests.post(auth_url, headers=headers, data=data)

# Print debug information to understand what went wrong
print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.text}")

# Obtain access token if the request is successful
if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access Token:", access_token)
else:
    print(f"Failed to get access token: {response.status_code}")
    access_token = None

# Function to get the Spotify playlist tracks


def get_spotify_playlist(playlist_id):
    if not access_token:
        print("No access token. Cannot fetch the playlist.")
        return None

    # Spotify API endpoint for retrieving playlist tracks
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Send GET request to fetch playlist tracks
    response = requests.get(playlist_url, headers=headers)

    if response.status_code == 200:
        playlist_data = response.json()
        return playlist_data
    else:
        print(f"Failed to retrieve playlist: {response.status_code}")
        return None
