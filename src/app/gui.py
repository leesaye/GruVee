import tkinter as tk

window = tk.Tk()

def getInput():
    input_year = year.get(1.0, "end-1c")
    input_country = country.get(1.0, "end-1c")

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

enterButton = tk.Button(window, text="Generate songs", command=getInput)
enterButton.pack()

window.mainloop()
