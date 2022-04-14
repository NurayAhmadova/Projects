# file = open("my_file.txt") this method requires closing the file afterwards using file.close()

# this method does not require to close the file:
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# in this case, it is important to specify the mood, as the default mode is read-only, as in above:
# this piece of code will delete the previous data and replace it with "New text."
# it is because "w" will only write, not append.
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# to append the new text the following mode is used:
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# if you are trying to write into a file that does not exist, it will be automatically created for you.
# it only works in "w" mode and if the file does not exist yet.
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
