# Bilal Sayed C950 PackageData.py

from HashTable import HashTable
from Package import Package
import csv


# create hash table
ht = HashTable(40)

# read package info into hash table
with open('package.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        ht.set(row[0], Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
