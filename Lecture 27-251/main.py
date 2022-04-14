from tkinter import *

# Pack - packs each of the widgets next to each other in a vaguely logical format
# by default it will always start from the top and then pack every other widget just below the previous one
# the problem with pack is that it is difficult to specify a precise position, you can only choose the side

# Place -  it is all about precise positioning. When you place something you can provide x and y value
# the downside of place is that it is so specific and we have to work out in out head
# the coordinate and where to put each widget

# Grid - imagines that you entire program is a grid and you can divide it into
# any number of columns and rows that you want to. The grid method is relative to other widgets


def button_clicked():
    new_text = user_input.get()
    print("I got clicked")
    label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


label = Label(text="I am a Label", font=("Arial", 24, "bold"))
label.config(text="New text 2")
label.grid(row=0, column=0)
label.config(padx=20, pady=20)


button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New button")
new_button.grid(row=0, column=2)

user_input = Entry(width=10)
user_input.grid(row=2, column=3)


window.mainloop()
