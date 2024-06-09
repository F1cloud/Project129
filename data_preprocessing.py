import csv

dataset_1 = []
dataset_2 = []

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("archive_dataset_sorted1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

#combine the archive sorted files based on index number
#index number 1 will be combined with index number 1
headers = headers_1 + headers_2
planet_data = []
#enumberate - returns both index value and what is the data
for index, data_row in enumerate(planet_data_1):
    #index value should be same - to append the data
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("merge_data.csv", "a+") as f:
    #doing it one by one which is why its in append mode
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

    