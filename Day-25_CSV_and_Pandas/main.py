
# with open("Day-25_CSV/weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("Day-25_CSV/weather_data.csv") as file:
#     data= csv.reader(file)
#     print(data)

#     temperature = []
#     for row in data:
#         if row[1]!="temp":
#             a = int(row[1])
#             temperature.append(a)
#     print(temperature)
    
# import pandas as pd
# data = pd.read_csv("Day-25_CSV_and_Pandas/weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list=data["temp"].to_list()
# one can find the average of any column by using the mean() function and also by diving the sum by the length of the list 
# temp_mean=data["temp"].mean() 
# average= sum(temp_list)/len(temp_list)

# print(temp_list)
# print(temp_mean)
# print(average)

# max_values=data["temp"].max()
# print(max_values)

# get data in column
# print(data.day)

# get data in row
# print(data[data.day=="Monday"])

# print the highest temperature row
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# monday_temp=monday.temp[0]
# far=monday_temp*9/5 + 32
# print(far)

# data={'name':["A","B","C"],'age':[20,21,22]}
# df=pd.DataFrame(data)
# print(df)
# df.to_csv("Day-25_CSV_and_Pandas/new_data.csv",index=False)
 
import pandas as pd 
data=pd.read_csv("Day-25_CSV_and_Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels=data[data["Primary Fur Color"]=="Gray"]
cinnamon_squirrels=data[data["Primary Fur Color"]=="Cinnamon"]
black_squirrels=data[data["Primary Fur Color"]=="Black"]


print(len(grey_squirrels))
print(len(cinnamon_squirrels))
print(len(black_squirrels))

data_dict={
    "Fur Color": ["Grey","Cinnamon","Black"],
    "Count":[len(grey_squirrels),len(cinnamon_squirrels),len(black_squirrels)]
}

df=pd.DataFrame(data_dict)
df.to_csv("Day-25_CSV_and_Pandas/squirrel_count.csv")