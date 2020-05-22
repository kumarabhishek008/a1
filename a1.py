
n = int (input())
step = input()
print(step)
hills = 0
sealevel = 0


for i in step:
    if sealevel ==1  and i == 'd':
        hills +=1
    if i =='u':
        sealevel +=1
    else:
        sealevel -=1
print(hills)

arr = [[],[],[],[]]
for i in range(1):
    arr[i].append("12")
print(arr)