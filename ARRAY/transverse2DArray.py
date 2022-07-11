import numpy as np
twoDArray = np.array([[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]])
print(twoDArray)

def tranversetwoDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

tranversetwoDArray(twoDArray)
