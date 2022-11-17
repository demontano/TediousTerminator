import csv

#Grabs info from .csv ( info pulled from 'amms' )
data = []
with open('Master.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

with open('AssetTags.txt') as asset:
    bigList = [line.strip() for line in asset]

#if tag from txt file is in the csv col [1] , it'll add it will append the name/asset/sn/site to new csv.
col = [x[1] for x in data]
final = list()
for tag in bigList:
    if tag in col:
        for x in range(0, len(data)):
            if tag == data[x][1]:
                print(data[x])
                final.extend(data[x])
                with open('!!!Completed.csv', 'a') as f:
                    writer_object = csv.writer(f, lineterminator='\n')
                    writer_object.writerow(data[x])
                    f.close()

    else:
        with open('!!!Missing.csv', 'a') as f:
            writer_object = csv.writer(f, lineterminator='\n')
            writer_object.writerow(tag)
            f.close()


