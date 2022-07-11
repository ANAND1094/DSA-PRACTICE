myList = [1,2,3,4,5,6,7,8,9,1,11,12,13,14,18,19]
#print(myList)

def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True
print(isUnique(myList))