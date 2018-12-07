import matplotlib.pyplot as plt

setup="""

import random

def mergeSort(x):

    if len(x) > 1:
       
       middle = len(x)//2
       L = x[:middle]
       R = mergeSort(x[middle:])
       
       mergeSort(L)
       mergeSort(R)
       
       i  = j = k =0
       
       while i < len(L) and j < len(R):
           if L[i] < R[j]:
               x[k] = L[i]
               i+=1
       
           else:
               x[k] = R[j]
               j+=1
           k+=1 
       while i < len(L):
            x[k] = L[i]
            i+=1
            k+=1
       while j < len(R):
            x[k]=R[j]
            j+=1
            k+=1


def printList(x):
    for i in range (len(x)):
        print(x[i])
        print()
        
        
def MeasureThis(size):
    myList=[]
    for i in range(size):
        myList.append(random.randint(0,size))
        
"""


import timeit
TimeMerge=timeit.Timer("MeasureThis(1000)", setup=setup)
print (TimeMerge.timeit(5))


