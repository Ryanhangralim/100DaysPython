import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {}
data_dict["Fur Color"] = ["grey", "red", "black"]
data_dict["Count"] = [gray_count, red_count, black_count]

squirrel = pandas.DataFrame(data_dict)
squirrel.to_csv("squirrel_count.csv")