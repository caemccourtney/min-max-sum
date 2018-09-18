import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.

def quicksort(arr):
    
    if len(arr)<=1:
        return arr
    
    smaller,equal,larger=[],[],[]
    
    pivot = arr[0]
    
    for x in arr:
        if x<pivot:
            smaller.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            larger.append(x)
            
    return quicksort(smaller)+equal+quicksort(larger)


def miniMaxSum(arr):

    sorted_array = quicksort(arr)
    
    min_sum = sum(sorted_array[0:4])
    max_sum = sum(sorted_array[::-1][0:4])

    return min_sum, max_sum
    

    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))