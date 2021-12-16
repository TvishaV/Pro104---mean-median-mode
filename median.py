import csv

with open(r"covid19-cases.csv",newline = "") as df:
    datareader = csv.reader(df)
    all_data = list(datareader)

all_data.pop(0)

cases_data = []

for i in range(len(all_data)):
    cases = all_data[i][1]
    cases_data.append(cases)

cases_data.sort()

n = len(cases_data)

if n % 2 == 0:
    median_1 = float(cases_data[n//2])
    median_2 = float(cases_data[n//2-1])
    median = (median_1+median_2)/2

else:
    median = float(cases_data[n//2])

print(median)