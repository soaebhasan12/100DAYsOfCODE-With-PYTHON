## The Great Squirrel Census Data Analysis (with Pandas!)

## Challenge: How many gray, cinnamon and black squirrels in given data-set based on "Primary Fur Color", take this data and build new Dataframe of this data named "squirrel_count.csv"

import pandas

data = pandas.read_csv("004 Day-25/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, Cinnamon_squirrels_count, Black_squirrels_count]
}

DF = pandas.DataFrame(data_dict)
print(DF)
DF.to_csv("004 Day-25/squirrel_count.csv")