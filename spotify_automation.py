import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="http://localhost:8080",  # Set this in Spotify Dev settings
    scope="playlist-modify-public"
))

# Fetch new songs from a specific artist
def get_latest_tracks(artist_name):
    results = sp.search(q=f"artist:{artist_name}", type="track", limit=10)
    tracks = [item['uri'] for item in results['tracks']['items']]
    return tracks

# Update playlist with new tracks
def update_playlist(playlist_id, track_uris):
    sp.playlist_replace_items(playlist_id, track_uris)

if __name__ == "__main__":
    # Replace these with your playlist ID and artist
    playlist_id = "YOUR_PLAYLIST_ID"
    artist_name = "Coldplay"

    new_tracks = get_latest_tracks(artist_name)
    update_playlist(playlist_id, new_tracks)
    print("Playlist updated successfully!")
