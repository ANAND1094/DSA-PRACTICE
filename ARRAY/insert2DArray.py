from matplotlib.pyplot import axis
import numpy as np
twoDArray = np.array([[11, 12, 13, 14],[10, 14, 11, 21],[55, 55, 44, 66],[77, 565, 55, 44]])
print(twoDArray)

#newTwoDArray =  np.insert(twoDArray,2,[[1,2,3,4]],axis=0)
#axis=0 is for row and axis=1 is for column
#print(newTwoDArray)

#instend of insert we use append and it will add to the last
newTwoDArray =  np.append(twoDArray,[[1,2,3,4]],axis=0)
print(newTwoDArray)