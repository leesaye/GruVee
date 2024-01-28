import tkinter as tk
import apiAccess

window = tk.Tk()

def generate_songs():
    input_year = year.get(1.0, "end-1c")
    input_country = country.get(1.0, "end-1c")

    songs = apiAccess.get_songs(input_year, input_country)

    songs_str = ""

    for song in songs:
        songs_str += song + " - " + songs[song] + "\n"

    songs_label.config(text = songs_str)

    result_label.pack()
    songs_label.pack()




window.title("GruVee")
window.geometry('400x200')

year_label = tk.Label(text="Enter a decade (eg 2010s)")
year = tk.Text(window, height=1, width=10)
year_label.pack()
year.pack()

country_label = tk.Label(text="Enter a country you miss")
country = tk.Text(window, height=1, width=20)
country_label.pack()
country.pack()

enterButton = tk.Button(window, text="Generate songs", command=generate_songs)
enterButton.pack()

result_label = tk.Label(window, text="Here are your songs:")
songs_label = tk.Label(window, text="")

window.mainloop()
