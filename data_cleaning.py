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
f=open("/home/spiglobal/ACTA_NEUROLOGICA_SCANDINAVICA.txt")
file_reader= csv.reader(f, delimiter='|')
article_id=[]
journal_title=[]
journal_doi=[]
article_title=[]
article_body=[]
records=[]
for line in file_reader:
    article_id.append(line[0])
    journal_doi.append(line[2])
    article_title.append(line[3])
    article_body.append(line[4])
    records.append(line)
removed_records=[]
perfect_records=[]
print(article_title[0])
print(len(article_title[0].split()))
count_removed_records=0
count_pr=0
for line in records:
    if(len(line[4].split())<5):
        count_removed_records=count_removed_records+1
        removed_records.append(line)
    else:
        perfect_records.append(line)
        count_pr=count_pr+1
"""
for line in removed_records:
    print(line)
print(count_removed_records)
    
"""
word_count=0
for line in perfect_records:
    word_count+=len(line[4].split())
print("Number of empty records is",count_removed_records-1)
print("Number of proper records is",count_pr-1)
print(word_count)
print(count_pr)
print("The average article length is",word_count/count_pr)