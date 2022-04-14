import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# average_temp = round(sum(temp_list)/len(temp_list))
# print(average_temp)

print(data["temp"].mean())

print(data["temp"].max())

# this
print(data["condition"])
# is the same as this:
print(data.condition)

# get data in the rows
print((data[data.day == "Monday"]))

# row with the highest temp of the week
print(data[data.temp == data.temp.max()])

# getting hold of a certain parameter from the row
monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp_F = monday.temp * 1.8 + 32
print(monday_temp_F)

# create a dataframe from scratch
data_dictionary = {
    "student": ["Any", "James", "Angela"],
    "scores": [76, 56, 65],
}
student_data = pandas.DataFrame(data_dictionary)
data.to_csv("new_data.csv")
