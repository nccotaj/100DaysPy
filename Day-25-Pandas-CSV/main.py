# # data = []

# # with open("weather_data.csv") as file:
# #     data.append(file.readlines())

# # print(data)

# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)      #Creates a reader object that can be looped through
# #     next(data)
# #     temps = []
# #     for row in data:
# #         temps.append(int(row[1]))

# # print(temps)


# #Using Pandas

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])


# #series is 1 dimensional and dataframe is 2 dimensional

# #get Data in column
# data_dict = data.to_dict()
# #print(data_dict)

# temp_list = data["temp"].to_list()
# #print(len(temp_list))

# #print(data["temp"].mean())

# #print(data.temp.max())


# #get data in rows
# #print(data[data.day == "Monday"])

# #print(data[data.temp == data.temp.max()])  #Prints the row with the max temp

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0] 

# print(monday_temp)
# monday_farenheight = monday_temp * 9/5 + 32

# print(monday_farenheight)


# ##
# #create dataframe
# ##

# score_dict = {
#     "students":["Amy","Jeff","Sam"],
#     "scores":[76,56,100]
# }

# score_data = pandas.DataFrame(score_dict)

# score_data.to_csv("score_data.csv")



import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

color_data = pandas.DataFrame(data_dict)

print(color_data)