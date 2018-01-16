#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:33:27 2018

@author: Jiawei Zhong
"""
"""
import csv
with open('unsorted.txt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
 """
 # Open unsorted file and convert the data to 2D array
import copy

f = open("unsorted.txt")
arr = []
for line in f.readlines():
    line = line.strip()
    temp = line.split(",")
    arr.append(temp)

# Define quicksort function    
def quicksort(arr, rank, i, j):
    if i >= j:
        return
    lo = i
    hi = j
    pivot = int(arr[hi][rank])
    pivot_record = copy.deepcopy(arr[hi])

    while lo < hi:
        while lo < hi and int(arr[lo][rank]) < pivot:
            lo = lo + 1
        if lo == hi: # If arr is well partited
            break
        else:
            arr[hi] = arr[lo]
            hi = hi - 1
        
        if lo == hi:
            break
        
        while lo < hi and int(arr[hi][rank]) >= pivot:
            hi = hi - 1
        if lo == hi:
            break
        else:
            arr[lo] = arr[hi]
            lo = lo + 1
                     
    arr[hi] = pivot_record
    quicksort(arr, rank, i, hi-1)
    quicksort(arr, rank, hi, j)
    return
# Do the quicksort
quicksort(arr, 2, 0, len(arr)-1)