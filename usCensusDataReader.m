filename = 'Workbook1.csv';
fileID = fopen(filename);
mydata = textscan(fileID);
fclose(fileID);