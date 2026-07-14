from tkinter import *
from PIL import Image, ImageTk


window = Tk()
#WINDOW
logo = PhotoImage(file="logo.png")
window.iconphoto(True, logo)
window.title("Temperature Converter")
window.resizable(True, True)

#TITLE

icon = Image.open("logo.png")
icon = icon.resize((25,25))
icon = ImageTk.PhotoImage(icon)

title = Label(window,
              font=('Arial', 15, 'bold'),
              image=icon,
              text="Temperature Converter Tool",
              compound="left",
              relief=RIDGE,
              bd=5,
              padx=5,
              pady=5
              )
title.grid(row=0, column=0, columnspan=3, padx= 5, pady=5)

#CELsius TO FAHRENHEIT

celsiusTitle = Label(window,
                text=" Celsius To Fahrenheit ",
                font=('arial', 12, 'bold'),
                relief=RAISED,
                bd=2)
celsiusTitle.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

celsiusPrompt = Label(window,
                      text="Enter temperature in °C",
                      font=('arial', 10))
celsiusPrompt.grid(row=2, column=0, padx=5, pady=5)

celsiusEntry = Entry(window,
                     width=10,
                     )
celsiusEntry.grid(row=2, column=1, padx=5, pady=5)

def celsiusToFahrenheit():
    celsius = celsiusEntry.get()
    if celsius == "":
        celsiusResult.config(text="Please enter a value to convert.")
    else:
        try:
            fahrenheit = float(celsius)*(9/5) + 32
            celsiusResult.config(text=f"Your answer is {fahrenheit:.2f}°F")
        except ValueError:
            celsiusResult.config(text="Please enter a valid number.")
    
celsiusConvert = Button(window,
                        text="Convert",
                        command=celsiusToFahrenheit)
celsiusConvert.grid(row=2, column=2, padx=5, pady=5)

celsiusResult = Label(window,
                      text="",
                      font=('arial', 10, 'bold'))
celsiusResult.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

#FAHRENHEIT TO CELsius

fahrenheitTitle = Label(window,
                text=" Fahrenheit to Celsius ",
                font=('arial', 12, 'bold'),
                relief=RAISED,
                bd=2)
fahrenheitTitle.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

fahrenheitPrompt = Label(window,
                      text="Enter temperature in °F",
                      font=('arial', 10))
fahrenheitPrompt.grid(row=5, column=0, padx=5, pady=5)

fahrenheitEntry = Entry(window,
                     width=10,
                     )
fahrenheitEntry.grid(row=5, column=1, padx=5, pady=5)

def FahrenheitToCelsius():
    fahrenheit = fahrenheitEntry.get()
    if fahrenheit == "":
        fahrenheitResult.config(text="Please enter a value to convert.")
    else:
        try:
            celsius = (float(fahrenheit)-32)*5/9
            fahrenheitResult.config(text=f"Your answer is {celsius:.2f}°C")
        except ValueError:
            fahrenheitResult.config(text="Please enter a valid number.")
    
fahrenheitConvert = Button(window,
                        text="Convert",
                        command=FahrenheitToCelsius)
fahrenheitConvert.grid(row=5, column=2, padx=5, pady=5)

fahrenheitResult = Label(window,
                      text="",
                      font=('arial', 10, 'bold'))
fahrenheitResult.grid(row=6, column=0, columnspan=3, padx=5, pady=5)
window.mainloop()

