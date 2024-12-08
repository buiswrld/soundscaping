import os
from dotenv import load_dotenv
import spotipy

load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_sercet = os.getenv('SPOTIFY_CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_sercet))

def get_popularity(album: str) -> int:
    results = sp.search(q=album, type='album', limit=1)
    try:
        album_id = results['albums']['items'][0]['id']
        album_details = sp.album(album_id)
        return album_details['popularity']
    except IndexError:
        print("Error: Album not found")
        return None



