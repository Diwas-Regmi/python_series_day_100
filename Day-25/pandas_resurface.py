# with open("weather_data.csv") as file:
#     lines = [line.rstrip("\n") for line in file.readlines()]
#
#
# print(lines)

# import csv
# with open("weather_data.csv") as file:
#     temperature = []
#     data = csv.reader(file)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas as pd
data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].to_list()
# print(f"the average temperature in temperature list is {data["temp"].mean()}")
# max_value = data['temp'].max()
# print(f"the max temperature in temperature list is {max_value}")
# print(data.temp)
# print(data.day == "Monday")
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# data["temp_f"] = ((data["temp"] * 9/5) + 32)
# monday = data[data.day == "Monday"]
# print(monday.temp_f)
# print(monday.temp_f[0])
# # print(monday.temp_f)

#Create a dataframe from scratch
data_list = pd.DataFrame({
    "Name": ["Diwas", "Unik", "tutnu"],
    "Roll_no": [1,2,3],
    "age" : [23,20,22]
})
data_list.to_csv("my_personal_info.csv")