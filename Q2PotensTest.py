# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:08:27 2020

@author: PARTH
"""
A=[1,2,6,9,3]
sum=13
arr_size = len(A)
def Q2(A, arr_size, sum):
    for i in range( 0, arr_size-2):
        for j in range(i + 1, arr_size-1): 
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Numbers are:",A[i],",",A[j],",",A[k])
                    return True
    return False
Q2(A, arr_size, sum)