import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REFIRECT_URI"),
    scope="playlist-modify-public"
))

import random

def get_random_artist(genre):
    results = sp.search(q=f"genre:{genre}", type="artist", limit=50)  # Fixed line
    artists = [item['name'] for item in results['artists']['items']]
    return random.choice(artists)

def get_lastest_tracks():
    artist_name = get_random_artist("Indie")
    results = sp.search(q=f"artist:{artist_name}", type="track", limit=50)
    tracks = [item['uri'] for item in results ['tracks']['items']]
    return tracks

# Update playlist with new tracks
def update_playlist(playlist_id, track_uris):
    sp.playlist_replace_items(playlist_id, track_uris)

if __name__ == "__main__":
    # Replace these with your playlist ID and artist
    playlist_id = "1uVDlECu4Gbl1ggbK0HN40"  # Corrected playlist ID
    new_tracks = get_lastest_tracks()
    update_playlist(playlist_id, new_tracks)
    print("Playlist updated successfully!")
