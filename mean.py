import csv

with open(r"covid19-cases.csv",newline="") as f:
    data_reader = csv.reader(f)
    all_data = list(data_reader)

all_data.pop(0)

cases_data = []

for i in range(len(all_data)):
    cases = all_data[i][1]
    cases_data.append(float(cases))

totalCases = 0

for case in cases_data:
    totalCases += case

n = len(cases_data)    

mean = totalCases/n
print(mean)
