# data pre processing is the process of transforming raw data into an understanable format
import csv

dataset_1 = []
dataset_2 = []

with open("dataset_1.csv","r") as f:
    c = csv.reader(f)
    for i in c:
        dataset_1.append(i)

with open("sorted.csv","r") as f:
    c = csv.reader(f)
    for i in c:
        dataset_2.append(i)

headers1 = dataset_1[0]
planet_data1 = dataset_1[1:]

headers2 = dataset_2[0]
planet_data2 = dataset_2[1:]

headers = headers1 + headers2
planet_data = []
for index,data in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("final.csv","a+") as f:
    c = csv.writer(f)
    c.writerow(headers)   
    c.writerows(planet_data) 