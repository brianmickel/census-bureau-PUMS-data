"""
import csv
with open('ss14pca.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
  print(', '.join(row))


with open('ss14pca.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
  print(row['first_name'], row['last_name'])
"""


#ifile  = open('sample.csv', "rt", encoding=<theencodingofthefile>)

#works!!!!

import csv
pumsFile = open('ss14pca.csv', 'rt')
reader = csv.reader(pumsFile)
headers = next(reader)
print(headers)
column = {}
for h in headers:
    column[h] = []
#column
#{'first degree': [], 'employment status': [], 'wage': []}
for row in reader:
    for h, v in zip(headers, row):
        column[h].append(v)
print(column)


# for row in reader:
#         content = list(row[i] for i in included_cols)
#         print content
