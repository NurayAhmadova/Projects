import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# label.pack(expand=True)
label.pack(side="left")


# Advanced Python Arguments
# used to specify a wider range of inputs
# there are arguments with default input values that are fixed, hence changing them is optional, but possible

# Unlimited positional arguments (*args), args are a tuple
def add(*args):
    print(args[0])
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args


print(add(4, 5, 10))


# Unlimited keyword arguments (**kwargs), kwargs are a dictionary
def calculate(n, **kwargs):
    print((kwargs["add"]))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


# creating a class with initialized default input values
class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        # if we use .get() function, if a key value does not exist in the dictionary,
        # it will just return none, without giving an error
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car( model="GT-R")
print(my_car.make)

window.mainloop()
