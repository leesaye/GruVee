import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_songs(year: str, country: str) -> dict[str: str]:
    songs = {}
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # q = String.init(format:"artist:%@ track:%@", artistName, trackName)

    search_query = 'year:' + year + ' genre:' + country
    results = sp.search(q=search_query)
    # results = sp.search(q=f'genre: {genre}&year: {year}', limit=10, type="track")

    print(results)
    if len(results["tracks"]["items"]) == 0:
        return {}

    for i in range(0, len(results["tracks"]["items"])):
        track_name = results["tracks"]["items"][i]["name"]
        artist = results["tracks"]["items"][i]["artists"][0]["name"]
        songs[track_name] = artist
        # explicit = results["tracks"]["items"][i]['explicit']

    # image =

    # with open("testestest.json", "w") as text_file:
    #     text_file.write(str(results))
    #     text_file.close()

    # print(results["tracks"])
    return songs
