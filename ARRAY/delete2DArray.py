import numpy as np
twoDArray = np.array([[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]])
print(twoDArray)

newtwoDArray = np.delete(twoDArray, 0, axis = 0)
print(newtwoDArray)