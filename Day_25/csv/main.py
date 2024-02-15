# with open("weather_data.csv", "r") as file:
#     weathers = file.readlines()

# data = []
# for weather in weathers:
#     data.append(weather)

# import csv

# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for item in data:
#         if item[1] != "temp":
#             temperatures.append(int(item[1]))
#     print(temperatures) 

import pandas

data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# import math

# temp_list = data["temp"].to_list()
# print(data["temp"].max())

# #get data in column
# print(data["condition"])
# print(data.condition)

#get data in row
#prints row of data where day is Monday
# print(data[data.day == "Monday"])

# #prints row of data where temp is max
# print(data[data.temp == data.temp.max()])

#gets monday's temperature and conver it to fahrenheit
monday = data[data.day == "Monday"]
temp = (monday.temp * 1.8) + 32
print(temp + 1) 

#create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)