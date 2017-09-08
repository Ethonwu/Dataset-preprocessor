#!/usr/bin/env python
import os
import csv
f = open('STOCK_DAY_ALL.csv', 'r')
for row in csv.reader(f):
    print row
f.close()

