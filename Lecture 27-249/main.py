from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# label.pack(expand=True)
label.pack()

# changing the configurations of an object already created
label["text"] = "New text"
label.config(text="New text 2")


# Button
# def button_clicked():
#     print("I got clicked")
#     label.config(text="Button got clicked")

def button_clicked():
    new_text = user_input.get()
    print("I got clicked")
    label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()


# Entry
user_input = Entry(width=10)
user_input.pack()





window.mainloop()
