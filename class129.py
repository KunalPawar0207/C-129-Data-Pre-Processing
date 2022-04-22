# data pre processing is the process of transforming raw data into an understanable format
import csv
data = []
with open("dataset_2.csv") as f:
    c = csv.reader(f)
    for i in c:
        data.append(i)

headers = data[0]
planet_data = data[1:]

for d in planet_data:
    d[2] = d[2].lower()

planet_data.sort(key = lambda planet_data:planet_data[2])

with open("sorted.csv","a+") as f:
    c = csv.writer(f)
    c.writerow(headers)
    c.writerows(planet_data)

