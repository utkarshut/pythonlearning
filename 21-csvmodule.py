import csv
name = []
with open('20-Real-life example.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = '\t')
    next(csvReader)    # for printing from next line
    for line in csvReader:
        print(line)   # index of item


with open('20-Real-life example.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    with open('20-Real-life example-new.csv', 'w') as newFile:
        csvwriter = csv.writer(newFile, delimiter = '\t')
        for line in csvReader:
            csvwriter.writerow(line)

#dictreader

with open('20-Real-life example.csv', 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for line in csvReader:
        print(line['Price'])   # index of item

#DictWriter
with open('20-Real-life example.csv', 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    with open('20-Real-life example-newdictwriter.csv', 'w') as newFile:
        fieldName = ['Price', 'EngineV', 'Model', 'Year', 'Engine Type', 'Mileage', 'Body', '\ufeffBrand']
        csvwriter = csv.DictWriter(newFile, fieldnames=fieldName, delimiter = '\t')
        csvwriter.writeheader()
        for line in csvReader:
            name.append('{} year {} model'.format(line['Year'], line['Model']))
            del line['Registration']
            csvwriter.writerow(line)
print(name)

#by this we can also generate html accordingly --- practice