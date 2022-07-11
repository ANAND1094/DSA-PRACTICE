from operator import index


myList = [1,2,3,4,5,6,7,8,9]
print(myList)

#1.Searching for an Elemeny using "IN" Operator in the list
print("Step1")
if 9 in myList:
    print(myList.index(9))
else:
    print("The value does not exist in the list")


#2.Searching for an Elemeny using "Linear Search" Operator in the list
print("Step2")
def searchingList(list,value):
    for i in list:
        if i == value:
            return list.index(value)
    else:
        return"The value does not exist inthe list"
print(searchingList(myList,7))


#List Operations / Function
#3.Using "+"" operators to add 2 or more list in a list
print("Step3")
a = [1,2,3]
b = [4,5,6]
c = a + b 
print(c)

#4. Using "*" operator 
print("Step4")
d = c *5
print(d)

#5. Finding the length of list by len() method
print("Step5")
print(len(c))

#6. Finding the maximum value of list by max() method
print("Step6")
print(max(d))

#7. Finding the min value of list by sum() method
print("Step7")
print(min(c))

#8. Finding the sum of all list by sum() method
print("Step8")
print(sum(d))

#9. By the help of these operator we can perform many task eg average of all the number
print("Step9")
print(sum(a)/len(a))