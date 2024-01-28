import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_songs(year: str, country: str) -> dict[str: str]:
    songs = {}
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    search_query = 'year:' + year + ' genre:' + country
    results = sp.search(q=search_query)

    if len(results["tracks"]["items"]) == 0:
        return {}

    for i in range(0, len(results["tracks"]["items"])):
        track_name = results["tracks"]["items"][i]["name"]
        artist = results["tracks"]["items"][i]["artists"][0]["name"]
        songs[track_name] = artist

    return songs
