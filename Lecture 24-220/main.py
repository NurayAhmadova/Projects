# to open a file from a directory different than the project folder where ,ain.py is located:
with open("../../PycharmProjects/my_file.txt") as file:
    contents = file.read()
    print(contents)