#   CALCULATE AVERAGE TEMPRATURE

numDays = int(input("How many day's temprature? "))
total = 0
for i in range(1,numDays+1):
    nextDAy = int(input("DAy"+str(i)+"s high temp:"))
    total +=nextDAy

avg=round(total/numDays,2)
print("\nAverage ="+str(avg))