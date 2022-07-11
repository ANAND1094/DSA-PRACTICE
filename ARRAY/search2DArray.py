import numpy as np
twoDArray = np.array([[1,2,3,4,5,6],[11,22,33,44,55,66],[111,222,333,444,555,666]])
print(twoDArray)

def searchTwoDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):#we have given 0 here becuase it indicate no of column
            if array[i][j] == value:
                return "The value is located in the Index"+str(i)+""+str(j)
    return "The Element is not found"

print(searchTwoDArray(twoDArray,666))