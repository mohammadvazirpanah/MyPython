#!/usr/bin/python3

import csv
from collections import defaultdict
import sys

"""
Using the script:
python3 convpresence.py <input-file.csv>
The output will be placed in a file named 'presence-output.csv'
"""

presdict = defaultdict(dict)
dates = set()
with open(sys.argv[1], encoding="utf16", newline='') as incsv_file:
  csv_reader = csv.DictReader(incsv_file, delimiter='\t')
  for row in csv_reader:
    dates.add(row[' date-created'].split(' ')[1])
    presdict[row[' participant-name']]['name'] = row[' participant-name']
    presdict[row[' participant-name']][row[' date-created'].split(' ')[1]] = 'P'

dates_list = list(dates)
dates_list.sort()


fieldnames = ['name'] + dates_list

with open('presence-output.csv', 'w', encoding="utf16", newline='') as outcsv_file:
  csv_writer = csv.DictWriter(outcsv_file, fieldnames=fieldnames)
  csv_writer.writeheader()
  for student in presdict:
    csv_writer.writerow(presdict[student])
