import csv
import json

csvfile = open('SampleDataSales.csv', 'r')
jsonfile = open('ParsedCode.json', 'w')

fieldnames = ("Date","Time","Item Purchased","Bill Tendered","Change","Seller","Square")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write('\n')
