import csv

data = []

with open("archive_dataset.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
#1: - from 1 to the end
planet_data = data[1:]

#Converting all planet names to lower case
for data_point in planet_data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
#lambda - sort in alphabetical order and based on what data are you sorting
planet_data.sort(key=lambda planet_data: planet_data[2])

#a+ - append mode, finish 1, append it etc.
with open("sorted.csv", "a+") as f:
    #write the data one by one
    csvwriter = csv.writer(f)
    #first write headings then the panet data
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#remove blank lines
#sorted_1 - is output file and replacing newline with double quotes
with open('sorted.csv') as input, open('sorted1.csv', 'w', newline='') as output:
     #creating writer for csv file
     writer = csv.writer(output)
     #for the sorted file, opening each roe
     for row in csv.reader(input):
        #strip - blank line
        #only if there info, do you write it, if it is blank, you skip it 
        #remove unwanted line for you
         if any(field.strip() for field in row):
             writer.writerow(row)
