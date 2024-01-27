import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_songs(year: str, genre: str, vibe: str) -> dict[str: str]:

    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.search(q=f'genre: {genre}&year{year}', limit=10, type="track")

    print(results)

    return {
        "Tattoo": "Loreen",
        "Cha Cha Cha": "Kaarjia",
    }
