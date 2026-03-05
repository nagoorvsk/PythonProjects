import csv

rows = []

with open("/Users/shaik/Downloads/orders.csv","r",newline="") as file:
    reader = csv.reader(file)
    next(reader)
    rows = list(reader)

for row in rows:
    print(row[0])