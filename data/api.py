import os
from dotenv import load_dotenv
import spotipy

# References: (1), (2), (17), (18)
class SpotifyAPI:
    def __init__(self):
        """
        Initializes SpotifyAPI with client credentials. 
        Ensure that SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET are properly set and activated in the .env file.
        https://developer.spotify.com/documentation/web-api
        """
        load_dotenv()
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_sercet = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_sercet))

    def get_popularity(self, album: str) -> int:
        """
        Get the popularity of an album from the Spotify API.
        
        Parameters:
        album (str): The name of the album to search for.
        
        Returns:
        int: The popularity score of the album (0-100), or None if the album is not found.
        """
        results = self.sp.search(q=album, type='album', limit=1)
        try:
            album_id = results['albums']['items'][0]['id']
            album_details = self.sp.album(album_id)
            return album_details['popularity']
        except IndexError:
            print("Error: Album not found")
            return None



