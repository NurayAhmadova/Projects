import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


count_gray = len(data[data["Primary Fur Color"] == "Gray"])
count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black = len(data[data["Primary Fur Color"] == "Black"])

squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray, count_cinnamon, count_black]
}

df = pandas.DataFrame(squirrels_dict)
df.to_csv("squirrel_count.csv")
