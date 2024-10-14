from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import os

# Define the scope for YouTube Data API access
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME= 'youtube'
API_VERSION= 'v3'

# Function to authenticate with YouTube using OAuth 2.0
def get_authenticated_service():
    # The file 'client_secret.json' should contain your OAuth 2.0 credentials downloaded from the Google Cloud Console
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
    credentials = flow.run_local_server(port=0)  # Start the OAuth 2.0 server and authenticate
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

# Function to create a new YouTube playlist
def create_playlist(youtube, title, description):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["Spotify", "Converted Playlist"],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "public"  # Can also be "private" or "unlisted"
            }
        }
    )
    response = request.execute()
    print(f"Playlist created: {response['id']}")
    return response['id']

# Function to search for a video on YouTube by a given query (e.g., song name and artist)
def search_video(youtube, query):
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query,  # Search query (song name and artist)
        type="video"  # We want only videos, not channels or playlists
    )
    response = request.execute()
    
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        print(f"Found video for query '{query}': {video_id}")
        return video_id
    else:
        print(f"No video found for query: {query}")
        return None
    

# Function to add a video to a YouTube playlist
def add_video_to_playlist(youtube, playlist_id, video_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    response = request.execute()
    print(f"Added video to playlist: {response['snippet']['title']}")