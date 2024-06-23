import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = '-' # replace with your own client id
CLIENT_SECRET = '-' # replace with your own client secret
REDIRECT_URI = '-' # replace with your own redirect url/uri

SCOPE = 'playlist-modify-public playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

def add_song_to_playlist_multiple_times(playlist_id, track_id, repeat_count):
    for _ in range(repeat_count):
        sp.playlist_add_items(playlist_id, [track_id])

playlist_id = '-' # replace with id of your playlist, found in the playlist link
track_id = '03UrZgTINDqvnUMbbIMhql' # gangnam style. replace with song id, found in song link.

repeat_count = 10 # change to however many times you wanna add the song

add_song_to_playlist_multiple_times(playlist_id, track_id, repeat_count)

print(f"Added the song {repeat_count} times to the playlist.")
