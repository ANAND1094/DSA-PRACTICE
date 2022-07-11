#1.Creating a List
from re import S


print("Step1")
ShoppingList = ["Milk","Cheese","Butter","Salt","Apple"]
print(ShoppingList)

#2.Accesing A List Element
print("Step2")
print(ShoppingList[0])
print(ShoppingList[-1])

#3.Accessing a List Element Using "IN" operator
print("Step3")
print("Milk" in ShoppingList)#By this operator it will show Boolen (True,False)

#4.Transverse the List
print("Step4")
for i in ShoppingList:
    print(i)
print(ShoppingList)

#5.Transverse List using indexes--- by the help of this method we can also do some operations like mathematics
print("Step5")
#for i in range (len(ShoppingList)):
#    ShoppingList[i] = ShoppingList[i]+"+"
#   print(ShoppingList[i])

#6.Update In the List
print("Step6")
ShoppingList[2] = "Chocolate"
#ShoppingList[0] = 444
print(ShoppingList)

#7.Insertion in the list using "Insert(Index,Value)"Method
print("Step7")
ShoppingList.insert(1,"Rice")
print(ShoppingList)

#8.Insertion In the List By Using "append" Method
print("Step8")
ShoppingList.append("Banana")
print(ShoppingList)

#9.Insertion in the list by "Extend" Method>>By this Method we can add another list to this list
print("Step9")
newShoppingList = [1,2,3,4,5,6]
ShoppingList.extend(newShoppingList)
print(ShoppingList)

#10.Slicing in the list
print("Step 10")
print(ShoppingList[2:5])

#11.Update of element by Slicing
print("Step11")
ShoppingList[0:2] = ["Lock","Key"]
print(ShoppingList)

#12.Deletion a element through POP() method
print("Step12")
print(ShoppingList.pop(-1))
print(ShoppingList)

#13. Deletion of Element using del() method>>by this method we can delete more than 1 item by slicing
print("Step13")
#del ShoppingList[0:2]
#print(ShoppingList)

#14.Deletion of element by remove() method
print("Step14")
ShoppingList.remove("Salt")
print(ShoppingList)