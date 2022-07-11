from multiprocessing.sharedctypes import Value


myList = list()
while(True):
    inp = input("Enter a number: ")
    if inp == "done":break
    Value = float(inp)
    myList.append(Value)
average = sum(myList)/len(myList)
print("Average:",average)