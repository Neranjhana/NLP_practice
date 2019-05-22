#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:41:06 2019

@author: spiglobal
"""

import sys
import csv
import collections
csv.field_size_limit(sys.maxsize)
from numpy import array
f=open("/home/spiglobal/acta_pyschatria_scandinavia.txt")
file_reader= csv.reader(f, delimiter='|')
article_id=[]
journal_title=[]
journal_doi=[]
article_title=[]
article_body=[]
records=[]
for line in file_reader:
    article_id.append(line[0])
    journal_title.append(line[1])
    journal_doi.append(line[2])
    article_title.append(line[3])
    article_body.append(line[4])
    records.append(line)
removed_records=[]
perfect_records=[]
print(article_title[0])
print(len(article_title[0].split()))
count_removedrecords=0
for line in records:
    if(len(line[4].split())<5):
        count_removedrecords+1
        removed_records.append(line)
    else:
        perfect_records.append(line)
for line in removed_records:
    print(line)
print(count_removedrecords)
print("abc")