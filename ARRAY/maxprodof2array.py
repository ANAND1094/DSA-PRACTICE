# How to find max product of 2 int in the array where all element are positive

import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def findMaxProd(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) +","+ str(array[j])
    print(pairs)
    print(maxProduct)

findMaxProd(myArray)

