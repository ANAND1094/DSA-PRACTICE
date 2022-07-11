from array import *
arr1 = array('i',[1,2,3,4,9,6])

def searchInArray(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element is not there in this array"

print(searchInArray(arr1,9))
               