import os
from dotenv import load_dotenv
import spotipy

class SpotifyAPI:
    def __init__(self):
        load_dotenv()
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_sercet = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_sercet))

    def get_popularity(self, album: str) -> int:
        results = self.sp.search(q=album, type='album', limit=1)
        try:
            album_id = results['albums']['items'][0]['id']
            album_details = self.sp.album(album_id)
            return album_details['popularity']
        except IndexError:
            print("Error: Album not found")
            return None



