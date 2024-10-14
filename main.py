# Import necessary functions from other files
from spotify_auth import get_spotify_playlist
from youtube_playlist import get_authenticated_service, create_playlist, search_video, add_video_to_playlist


def main():
    # Spotify Playlist ID
    playlist_id = user_playlist

    # Step 1: Get Spotify Playlist Tracks
    print("Retrieving tracks from Spotify playlist...")
    spotify_tracks = get_spotify_playlist(playlist_id)
    if not spotify_tracks:
        print("Failed to retrieve Spotify playlist tracks.")
        return

    # Extract track details (e.g., "Song Name by Artist Name")
    track_list = [f"{item['track']['name']} by {
        item['track']['artists'][0]['name']}" for item in spotify_tracks['items']]

    # Step 2: Authenticate with YouTube
    print("Authenticating with YouTube...")
    youtube = get_authenticated_service()

    # Step 3: Create a new YouTube Playlist
    print("Creating YouTube playlist...")
    youtube_playlist_id = create_playlist(
        youtube, title="Spotify Converted Playlist", description="Playlist generated from Spotify")

    # Step 4: Search for each track on YouTube and add to playlist
    print("Adding videos to YouTube playlist...")
    for track in track_list:
        print(f"Searching for track: {track}")
        video_id = search_video(youtube, track)
        if video_id:
            add_video_to_playlist(youtube, youtube_playlist_id, video_id)
        else:
            print(f"Could not find YouTube video for: {track}")

    print(f"Playlist '{
          youtube_playlist_id}' successfully created and populated with tracks.")


user_playlist = input("Enter playlist you want to convert: ")
if __name__ == "__main__":
    main()
