from array import *

n = int (input ("enter the number of shocks -"))
ar = []
print("enter colors of shocks")
for i in range(n):

    a = int(input())
    ar.append(a)
print(ar)
arr1 =[]

for i in range(0,len(ar)-1,1) :
    for j in range(i,len(ar)-1,1):
        if ar[j+1]==ar[i]:
            n=ar[j+1]
            ar.remove(ar[j+1])
            arr1.append(n)

            break


print (arr1)