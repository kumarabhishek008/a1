'''
def dynamicarray(n,queries):
    seqlist = []
    d=[]
    e=[]
    empty_spaces = []
    for i in range(n):
        seqlist.append(empty_spaces)
    seqlist=[d,e]
    lastAnswer=
    newarr=[]0
    for i in range(len(queries)):
        if (queries[i][0] == 1):

            seq = (((queries[i][1])^lastAnswer)%n)
            if seq==0:
                d.append(queries[i][2])
            if seq==1:
                e.append(queries[i][2])
            print(seqlist)

        if (queries[i][0] == 2):

            seq = ((queries[i][1]^lastAnswer)%n)
            a = queries[i][2]
            lastAnswer=seqlist[seq][a]
            newarr.append(lastAnswer)
    return newarr


###########ekfmrklkltrrgltl#############
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
q = int(first_multiple_input[1])
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

print(dynamicarray(n,queries))'''



import math

def euler(val):
    val = str(val)
    a = 0;
    for i in val:
        a += math.factorial(int(i))
    a = str(a)
    b=0
    for i in a:
        b += int(i)
    return b
def check(n,m):
    Egi = 0
    for i in range(1,n+1):
        k=0
        for j in range(1,m):
            if i == euler(j):
                k = j
                break
        sgi = 0
        k = str(k)
        for l in k:
            sgi += int(l)
        Egi += sgi

    return Egi


q = int(input())

while q > 0:
    # Type below...
    nm = input()
    n = int(nm.split()[0])
    m = int(nm.split()[1])
    ########
    print(check(n, m))
    q -= 1
