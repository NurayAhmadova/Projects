from tkinter import *


def input_given():
    miles_input = float(user_input.get())
    miles_to_km = round(miles_input * 1.609, 2)
    km_output.config(text=f"{miles_to_km}")


window = Tk()
window.title("Miles to km Converter")
window.config(padx=20, pady=20)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

km = Label(text="Km")
km.grid(row=1, column=2)

user_input = Entry(width=7)
user_input.grid(row=0, column=1)

km_output = Label(text=0)
km_output.grid(row=1, column=1)

calculate = Button(text="Calculate", command=input_given)
calculate.grid(row=2, column=1)

window.mainloop()
