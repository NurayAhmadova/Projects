# Create the logging_decorator() function
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called a function{function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned {result}")
    return wrapper


# Use the decorator
@logging_decorator
def multiplication(a, b, c):
    return a * b * c


multiplication(2, 3, 4)
