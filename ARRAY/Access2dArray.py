import numpy as np

twoDArray = np.array([[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]])
print(twoDArray)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array(0)):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray,0,0)
