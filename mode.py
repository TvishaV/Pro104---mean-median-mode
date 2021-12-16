import csv
from collections import Counter

with open(r"covid19-cases.csv", newline = "") as df:
    data_reader = csv.reader(df)
    all_data = list(data_reader)

all_data.pop(0)

cases_data = []

for i in range(len(all_data)):
    cases = all_data[i][1]
    cases_data.append(cases)

cases_counter = Counter(cases_data)

cases_data_range = {
    "0-5000":0,
    "5000-10000":0,
    "10000-50000":0,
}

for case,occurence in cases_counter.items():
    if 0 < float(case) < 5000:
        cases_data_range["0-5000"]+= occurence

    elif 5000 < float(case) < 10000:
        cases_data_range["5000-10000"]+= occurence

    elif 10000< float(case) < 50000:
        cases_data_range["10000-50000"] += occurence

modeRange,modeOccurence = 0,0

for range,occurence in cases_data_range.items():
    if occurence > modeOccurence:
        modeRange,modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])] , occurence

mode = float((modeRange[0] + modeRange[1]) / 2)
print(mode)