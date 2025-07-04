# 002 Reading CSV Data in Python

# Challenge: Open the "weather-data.csv". Use .readlines() to create a list names data that cntains the values from the .csv file.

# with open(r"002 Day-25/weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)




# import csv

# with open(r"002 Day-25/weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(row[1])
#     print(tempratures)





import pandas

data = pandas.read_csv("002 Day-25/weather-data.csv")
print(data)
print(data["temp"])