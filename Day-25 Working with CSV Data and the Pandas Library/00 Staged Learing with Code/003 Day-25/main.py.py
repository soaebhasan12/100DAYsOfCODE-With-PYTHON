## 003 DataFrames & Series Working with Rows & Columns

import pandas

data = pandas.read_csv("002 Day-25/weather-data.csv")
print(data)
print(data["temp"])
print("\n")

print(type(data))
print(type(data["temp"]))
print("\n")

data_dict = data.to_dict()
print(data_dict)
print("\n")

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
print("\n")

## Challenge: Calculate the average temprature

# average = sum(temp_list) / len(temp_list)
# print(f"Average: {average}")

print(data["temp"].mean())
print("\n")


## Challenge: Find the maximum temprature from the temp_list.

print(data["temp"].max())
print("\n")


## Get Data in Columns

print(data["condition"])
print(data.condition)
print("\n")


## Get Data in Rows

print(data[data["day"] ==  "Monday"])
print(data[data.day == "Monday"])
print("\n")


## Challenge: print the row of data which had the highest tempratures.

print(data[data["temp"] == data["temp"].max()])
print(data[data.temp == data.temp.max()])
print("\n")






monday = data[data.day == "Monday"]
print(monday.condition)
print("\n")

## Challenge: Convert Moday's temprature to Fahrenheit.

monday = data[data.day ==  "Monday"]
mon_temp = int(monday.temp)
mon_farn_temp = mon_temp*9/5 + 32

print(f"Monday Temprature {mon_temp}C in Farenheit: {mon_farn_temp}F")
print("\n")



## Create a Dataframe from screatch

data_dict = {
    "students": ["Shahdab", "Asif", "Afjal"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("003 Day-25/new_data.csv")