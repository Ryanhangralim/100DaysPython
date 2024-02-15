# with open("weather_data.csv", "r") as file:
#     weathers = file.readlines()

# data = []
# for weather in weathers:
#     data.append(weather)

import csv

with open("weather_data.csv", "r") as file:
    data = csv.reader(file)
    temperatures = []
    for item in data:
        if item[1] != "temp":
            temperatures.append(int(item[1]))
    print(temperatures) 