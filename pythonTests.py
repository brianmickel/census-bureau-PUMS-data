import numpy
myDict = {
'0001': {
'salaries': [1,2,3],
'workHours': [10,20,30]
},
'0002': {
'salaries': [20,30,40],
'workHours': [100,200,300]
}
}
# myDict = {
# 0001: 2,
# 0002: 3
# }
print(myDict)
print(myDict['0001'])
print(myDict['0001']['salaries'])
print(numpy.mean(myDict['0001']['salaries']))
