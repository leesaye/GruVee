import apiAccess


def get_user_input() -> list[str]:
    """
    Get the user's inputs on their preferred year, genre, and vibe
    Returns year, genre, and vibe as a list of strings
    """
    print("Welcome to GruVee")

    year_is_valid = False

    while not year_is_valid:
        year = input("Enter a decade (eg 2010): ")

        if not year.isnumeric() or int(year) >= 2030:
            print("Please enter a valid year")
        else: # year < 2030
            year_is_valid = True

    genre = input("Enter a music genre: ")

    vibe = input("Enter the kind of vibe you want (eg sad): ")

    return [year, genre, vibe]


if __name__ == "__main__":
    user_inputs = get_user_input()

    userYear = user_inputs[0]
    userGenre = user_inputs[1].lower()
    userVibe = user_inputs[2].lower()

    songs = apiAccess.get_songs(userYear, userGenre, userVibe)

    print(f'\nHere are your recommended {userVibe} {userGenre} songs from the '
          f'{userYear}s:')

    for song in songs:
        print(f'{song} - {songs[song]}')
