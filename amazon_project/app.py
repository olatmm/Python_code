import csv
import json
from collections import namedtuple

""" Importing CSV file"""

with open('data.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    print(headings)
    for r in f_csv:
        print(r)
