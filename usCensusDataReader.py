import csv
filename = 'ss14pca.csv'
#filename = 'Workbook1.csv'
pumsFile = open(filename)
pumsFile_csv = csv.reader(pumsFile)
headers = next(pumsFile_csv)

#print(headers)
#column = {}
#for h in headers:
#    column[h] = []
#column
#{'first degree': [], 'employment status': [], 'wage': []}
# for row in pumsFile_csv:
#     for h, v in zip(headers, row):
#         column[h].append(v)
# print(column)


importantHeaders = ['FOD1P', 'ESR','WAGP','WKHP','OCCP','NAICSP']
print(headers)
#find indexes of columns
importantColumnsIndexes = []
for element in importantHeaders:
    importantColumnsIndexes.append( headers.index(element) )

print(importantColumnsIndexes)

#check that I got the right column numbers by comparing the terminal output
# importantColumnsHeaders = []
# for eachIndex in importantColumnsIndexes:
#     importantColumnsHeaders.append( headers[eachIndex] )
#
# print(importantHeaders)
# print(importantColumnsHeaders)
#end check !it's correct!


#keep important columns

appendableString = '['
for index in importantColumnsIndexes:
    addRowString = 'row['+ str(index)+']'
    appendableString = appendableString + addRowString + ','
#get rid of pesky comma at end
appendableString = appendableString[0:len(appendableString)-1]+']'
print(appendableString)

importantData = []
i = 0
for row in pumsFile_csv:
    if row[importantColumnsIndexes[0]] != '':
        importantData.append(eval(appendableString))
    i += 1
    print(i)

print(importantData[1:5])

row_count = sum(1 for eachRow in pumsFile_csv)
print('The length of the original dataset is: '+str(row_count))
print('The length of your dataset is: '+str(len(importantData)))

with open('collegeGradData.csv', 'w') as csvfile:
    mycsvwriter = csv.writer(csvfile, delimiter=',')
    mycsvwriter.writerows(importantData)


#
#
# for row in reader:
#         content = list(row[i] for i in included_cols)
#         print content
