import csv
import numpy
import matplotlib.pyplot as plt


filename = 'collegeGradData.csv'
#filename = 'Workbook1.csv'
collegeGradDataFile = open(filename)
collegeGradData_csv = csv.reader(collegeGradDataFile)
headers = ['FOD1P', 'ESR','WAGP','WKHP','OCCP','NAICSP']
i = 0
collegeGradData = []
for row in collegeGradData_csv:
    collegeGradData.append(row)
    i += 1
    print(i)



collegeGradDataEmployed = []
i = 0
for row in collegeGradData:
    if row[1] in ['1','2']:
        collegeGradDataEmployed.append(row)
    i += 1
    print('employed '+ str(i))

#compare visually
print(collegeGradData[1:20])
print(collegeGradDataEmployed[1:20])
# example ['6007', '1', '0090000', '46', '2830', '5191ZM']
collegeGradDataEmployedInt = [];
for row in collegeGradDataEmployed:
    collegeGradDataEmployedInt.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]])

for row in collegeGradDataEmployedInt:
    print(row)

listOfMajors = []
for row in collegeGradDataEmployedInt:
    listOfMajors.append(row[0])

listOfMajors = sorted(listOfMajors)
#print(listOfMajors)
listOfMajors = set(listOfMajors)

sortedDataByMajor = {}

print(listOfMajors)
for value in listOfMajors:
    print(value)
    # valueSalarySum = 0
    # valueSalaryCount = 0
    # valueWorkHoursSum = 0
    # valueWorkHoursCount = 0
    # for row in collegeGradDataEmployedInt:
    #     if row[0] == value:
    #         valueSalarySum = valueSalarySum + row[2]
    #         valueWorkHoursSum = valueWorkHoursSum + row[3]
    #         valueSalaryCount = valueSalaryCount + 1
    #         valueWorkHoursCount = valueSalaryCount + 1
    # valueSalaryAvg
    # valueWorkHoursAvg
    valueSalaryList = []
    valueWorkHoursList = []
    for row in collegeGradDataEmployedInt:
        if row[0] == value:
            valueSalaryList.append(row[2])
            valueWorkHoursList.append(row[3])

    sortedDataByMajor[str(value)] = {'salaries': valueSalaryList, 'workHours': valueWorkHoursList}

print(sortedDataByMajor['1100'])
print(sortedDataByMajor.items())

#np.around([1,2,3,11], decimals=1)

#start
filename = 'degreeCodes.csv'
#filename = 'Workbook1.csv'
degreeCodesFile = open(filename)
degreeCodesFile_csv = csv.reader(degreeCodesFile)
i = 0
degreeCodesData = {}

for row in degreeCodesFile_csv:
    degreeCodesData[row[0]] = row[1]
    i += 1
    print('degree code #: ' + str(i) + row[0] + row[1])
#end

#start
filename = 'occupationCodes.csv'
#filename = 'Workbook1.csv'
occupationCodesFile = open(filename)
occupationCodesFile_csv = csv.reader(occupationCodesFile)
i = 0
occupationCodesData = {}

for row in occupationCodesFile_csv:
    occupationCodesData[row[0]] = row[1]
    i += 1
    print('occupation code #: ' + str(i) + row[0] + row[1])
#end

for key, value in sortedDataByMajor.items():
    meanValueSalary = numpy.mean(value['salaries'])
    meanValueSalaryRounded = round(meanValueSalary, 2)
    meanValueWorkHours = numpy.mean(value['workHours'])
    meanValueWorkHoursRounded = round(meanValueWorkHours, 2)
    countOfEntries = len(value['salaries'])
    sortedDataByMajor[key]['meanSalary'] = meanValueSalaryRounded
    sortedDataByMajor[key]['meanWorkHours'] = meanValueWorkHoursRounded
    sortedDataByMajor[key]['countOfEntries'] = countOfEntries
    print(key)
    print([meanValueSalaryRounded,meanValueWorkHoursRounded,countOfEntries])
    #plt.hist(meanValueSalary, bins=10)
    fig = plt.figure()
    plotTitle = 'Histogram of Salary for key=' + key + ' name=' + degreeCodesData[key]
    plotTitle = plotTitle.replace("/", "-")
    plotTitle = plotTitle.replace(":", "-")
    plotFilename = plotTitle +'.png'
    plt.hist(value['salaries'])
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title(plotTitle)
    #plt.show()
    fig.savefig(plotFilename)
