#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:33:27 2018

@author: Jiawei Zhong
"""
 # Open unsorted file and convert the data to 2D array
f = open("unsorted.txt")
arr = []
for line in f.readlines():
    line = line.strip()
    temp = line.split(",")
    arr.append(temp)
f.close()
size = len(arr)

# Define quicksort function    
def quicksort(arr, rank, i, j):
    if i >= j:
        return
    if (i + 1 == j) and (int(arr[i][rank]) == int(arr[j][rank])):
        return
    lo = i
    hi = j
    pivot = int(arr[hi][rank])
    pivot_record = arr[hi][:]

    while lo < hi:
        while lo < hi and int(arr[lo][rank]) <= pivot:
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
quicksort(arr, 2, 0, size-1)

# Write file
f = open("sorted.txt", 'w')
for i in range(0, size):
    for j in range(0, 2):
        f.write(arr[i][j]+',')
    f.write(arr[i][j+1]+'\n')

f.close()
