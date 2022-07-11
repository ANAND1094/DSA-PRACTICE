from array import *

#1.Create a array and traverse
my_array = array('i',[1,2,3,4,5,6])
for i in my_array:
    print(i)

#2.Access individual element through index
print("Step2")
print(my_array[3])

#3.Append any value to the array using append() method
print("Step 3")
my_array.append(7)
print(my_array)

#4.Innsert value in an array using insert method()
print("Step4")
my_array.insert(2,88)#2 is index 88 is value
print(my_array)

#5.Exttndd pyton array using exted method
print("Step5")
my_array1 = array("i",[10,11,12])
my_array.extend(my_array1)
print(my_array)

#6. Add items from list into array using fromlist() method
print("Step6")
templist=[20,21,22]
my_array.fromlist(templist)
print(my_array)

#7. Remove any array element using remove() method
print("Step7")
my_array.remove(22)
print(my_array)

#8. Remove last array element using pop() method
print("Step8")
my_array.pop()
print(my_array)

#9. Fetch any element through it's index through index() method
print("Step9")
print(my_array.index(20))

#10. Reverse a python array using reverse() method.
print("Step10")
my_array.reverse()
print(my_array)

#11. Get array buffer information through buffer_info() method
print("step11")
print(my_array.buffer_info())

#12. Check for number of occurance of an eleement using count() method
print("Step12")
my_array.append(11)
print(my_array.count(11))

#13. Convert array to string using tostring/tobytes() method
print("Step13")
strtemp = my_array.tobytes()
print(strtemp)
ints = array('i')
ints.frombytes(strtemp)
print(ints)

#14.Convert array to a Python List with same element using Tolist() method
print("Step14")
#print(my_array.tolist())

#15. Append a string to char array using fromstring() method

#16. Slice Element from an Array
print("Step16")
print(my_array[0:5])

