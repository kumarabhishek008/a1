import numpy as np
from numpy import random

x = random.randint(9)
arr = np.array([1,2,3,4,5,6,7,8,9])
list = [0,1,2,3,4,5,6,7,8,9]
for i in range(4):
    a = int(input("input value = "))
    if i==0 and (a==1 or a==3 or a==7 or a==9 or a==2 or a==4 or a==6 or a==8):
        list.remove(a)
        list.insert(a,'x')
        list.remove(5)
        list.insert(5,'o')
        print("o=",5)
        print(list)
    if i==0 and a==5:
        list.remove(a)
        list.insert(a,'x')
        x = random.randint(1,9)
        if x != 5:
            print("o=",x)
            list.remove(x)
            list.insert(x,'o')
            print(list)
        else:
            print("o =",1)
            list.remove(1)
            list.insert(1,'o')
    if i==1:
        if list[5]!='x':
            if a==1 :
                list.remove(a)
                list.insert(a,'x')
                if list[3]=='x':
                    print("o=",2)
                    list.remove(2)
                    list.insert(2,'o')
                    print(list)
                if list[2]=='x':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3,'o')
                if list[4]=='x':
                    print("o=",7)
                    print(list)
                    list.remove(7)
                    list.insert(7,'o')
                if list[7]=='x':
                    print("o=",4)
                    list.remove(4)
                    list.insert(4,'o')
            if a==2:
                list.remove(a)
                list.insert(a,'x')
                if list[1]=='x':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3,'o')
                if list[3]=='x':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
            if a==4:
                list.remove(a)
                list.insert(a,'x')
                if list[1]=='x':
                    print("o=",7)
                    list.remove(7)
                    list.insert(7,'o')
                if list[7]=='x':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
            if a==6:
                list.remove(a)
                list.insert(a,'x')
                if list[9]=='x':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3,'o')
                if list[3]=='x':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9,'o')
            if a==8:
                list.remove(a)
                list.insert(a,'x')
                if list[7]=='x':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9,'o')
                if list[9]=='x':
                    print("o=",7)
                    list.remove(7)
                    list.insert(7,'o')
            if a==3:
                list.remove(a)
                list.insert(a,'x')
                if list[1]=='x':
                    print("o=",2)
                    list.remove(2)
                    list.insert(2,'o')
                if list[2]=='x':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
                if list[6]=='x':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9,'o')
                if list[9]=='x':
                    print("o=",6)
                    list.remove(6)
                    list.insert(6,'o')
            if a==7:
                list.remove(a)
                list.insert(a,'x')
                if list[1]=='x':
                    print("o=",4)
                    list.remove(4)
                    list.insert(4,'o')
                if list[4]=='x':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
                if list[8]=='x':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9,'o')
                if list[9]=='x':
                    print("o=",8)
                    list.remove(8)
                    list.insert(8,'o')
            if a==9:
                list.remove(a)
                list.insert(a,'x')
                if list[3]=='x':
                    print("o=",6)
                    list.remove(6)
                    list.insert(6,'o')
                if list[6]=='x':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3,'o')
                if list[8]=='x':
                    print("o=",7)
                    list.remove(7)
                    list.insert(7,'o')
                if list[7]=='x':
                    print("o=",8)
                    list.remove(8)
                    list.insert(8,'o')
        if list[5]=='x':
            if a==1:
                list.remove(a)
                list.insert(a,'x')
                print("o",9)
                list.remove(9)
                list.insert(9,'o')
            if a==2:
                list.remove(a)
                list.insert(a, 'x')
                print("o", 8)
                list.remove(8)
                list.insert(8, 'o')
            if a==3:
                list.remove(a)
                list.insert(a, 'x')
                print("o", 7)
                list.remove(7)
                list.insert(7, 'o')
            if a==4:
                list.remove(a)
                list.insert(a, 'x')
                print("o", 6)
                list.remove(6)
                list.insert(6, 'o')
            if a==6:
                list.remove(a)
                list.insert(a, 'x')
                print("o", 4)
                list.remove(4)
                list.insert(4, 'o')
            if a==7:
                list.remove(a)
                list.insert(a, 'x')
                print("o", 3)
                list.remove(3)
                list.insert(3, 'o')
            if a==8:
                list.remove(a)
                list.insert(a, 'x')
                print("o", 2)
                list.remove(2)
                list.insert(2, 'o')
            if a==9:
                list.remove(a)
                list.insert(a, 'x')
                print("o", 1)
                list.remove(1)
                list.insert(1, 'o')
    if i==2:
        if list[5]=='x':
            if a==1 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",9)
                list.remove(9)
                list.insert(9,'o')
            if a==2 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",8)
                list.remove(8)
                list.insert(8,'o')
            if a==3 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",7)
                list.remove(7)
                list.insert(7,'o')
            if a==4 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",6)
                list.remove(6)
                list.insert(6,'o')
            if a==6 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",4)
                list.remove(4)
                list.insert(4,'o')
            if a==7 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",3)
                list.remove(3)
                list.insert(3,'o')
            if a==8 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",2)
                list.remove(2)
                list.insert(2,'o')
            if a==9 :
                list.remove(a)
                list.insert(a,'x')
                print("o=",1)
                list.remove(1)
                list.insert(1,'o')
        if list[5]!='x':
            if a==1:
                if list[7]=='x' and list[8]=='x':
                    list.remove(a)
                    list.insert(a,'x')
                    if list[4]!='x' and list[4]!='o':
                        print("o=",4)
                        list.remove(4)
                        list.insert(4,'o')
                    else:
                        print("o=",6)
                        list.remove(6)
                        list.insert(6,'o')
                if list[3]=='x' and list[6]=='x':
                    list.remove(a)
                    list.insert(a,'x')
                    if list[8]!='x' and list[8]!='o':
                        print("o=",8)
                        list.remove(8)
                        list.insert(8,'o')
                    else:
                        print("o=",2)
                        list.remove(2)
                        list.insert(2,'o')
            if a==3:
                if list[9] == 'x' and list[8] == 'x':
                    list.remove(a)
                    list.insert(a,'x')
                    if list[6]!='x' and list[6]!='o':
                        print("o=",6)
                        list.remove(6)
                        list.insert(6,'o')
                    else:
                        print("o=",4)
                        list.remove(4)
                        list.insert(4,'o')
                if list[1]=='x' and list[4]=='x':
                    list.remove(a)
                    list.insert(a,'x')
                    if list[8]!='x' and list[8]!='o':
                        print("o=",8)
                        list.remove(8)
                        list.insert(8,'o')
                    else:
                        print("o=",2)
                        list.remove(2)
                        list.insert(2,'o')
            if a==7:
                if list[1] == 'x' and list[2] == 'x':
                    list.remove(a)
                    list.insert(a, 'x')
                    if list[4] != 'x' and list[4] != 'o':
                        print("o=", 4)
                        list.remove(4)
                        list.insert(4, 'o')
                    else:
                        print("o=", 6)
                        list.remove(6)
                        list.insert(6, 'o')
                if list[6]=='x' and list[9]=='x':
                    list.remove(a)
                    list.insert(a,'x')
                    if list[8]!='x' and list[8]!='o':
                        print("o=",8)
                        list.remove(8)
                        list.insert(8,'o')
                    else:
                        print("o=",2)
                        list.remove(2)
                        list.insert(2,'o')
            if a==9:
                if list[2] == 'x' and list[3] == 'x':
                    list.remove(a)
                    list.insert(a, 'x')
                    if list[6] != 'x' and list[6] != 'o':
                        print("o=", 6)
                        list.remove(6)
                        list.insert(6, 'o')
                    else:
                        print("o=", 4)
                        list.remove(4)
                        list.insert(4, 'o')
                if list[7]=='x' and list[4]=='x':
                    list.remove(a)
                    list.insert(a,'x')
                    if list[4]!='x' and list[4]!='o':
                        print("o=",8)
                        list.remove(8)
                        list.insert(8,'o')
                    else:
                        print("o=",2)
                        list.remove(2)
                        list.insert(2,'o')
            if a==2:
                if list[7] == 'x' and list[9] == 'x':
                    list.remove(a)
                    list.insert(a, 'x')
                    if list[4] != 'x' and list[4] != 'o':
                        print("o=", 4)
                        list.remove(4)
                        list.insert(4, 'o')
                    else:
                        print("o=", 6)
                        list.remove(6)
                        list.insert(6, 'o')
            if a==4:
                if list[3] == 'x' and list[9] == 'x':
                    list.remove(a)
                    list.insert(a, 'x')
                    if list[2] != 'x' and list[2] != 'o':
                        print("o=", 2)
                        list.remove(2)
                        list.insert(2, 'o')
                    else:
                        print("o=", 2)
                        list.remove(2)
                        list.insert(2, 'o')
            if a==6:
                if list[1] == 'x' and list[7] == 'x':
                    list.remove(a)
                    list.insert(a, 'x')
                    if list[2] != 'x' and list[2] != 'o':
                        print("o=", 2)
                        list.remove(2)
                        list.insert(2, 'o')
                    else:
                        print("o=", 8)
                        list.remove(8)
                        list.insert(8, 'o')
            if a==8:
                if list[1] == 'x' and list[3] == 'x':
                    list.remove(a)
                    list.insert(a, 'x')
                    if list[4] != 'x' and list[4] != 'o':
                        print("o=", 4)
                        list.remove(4)
                        list.insert(4, 'o')
                    else:
                        print("o=", 6)
                        list.remove(6)
                        list.insert(6, 'o')
    if i==3:
        if list[5]!='x':
            if a==2:
                list.remove(a)
                list.insert(a,'x')
                if list[1]!='x' and list[1]!='o':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
                if list[3]!='x' and list[3]!='o':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3, 'o')
                if list[7] != 'x' and list[7] != 'o':
                    print("o=", 7)
                    list.remove(7)
                    list.insert(7, 'o')
                if list[9]!='x' and list[9]!='o':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9, 'o')
            if a==4:
                list.remove(a)
                list.insert(a,'x')
                if list[1]!='x' and list[1]!='o':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
                if list[3]!='x' and list[3]!='o':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3, 'o')
                if list[7] != 'x' and list[7] != 'o':
                    print("o=", 7)
                    list.remove(7)
                    list.insert(7, 'o')
                if list[9]!='x' and list[9]!='o':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9, 'o')
            if a==6:
                list.remove(a)
                list.insert(a,'x')
                if list[1]!='x' and list[1]!='o':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
                if list[3]!='x' and list[3]!='o':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3, 'o')
                if list[7] != 'x' and list[7] != 'o':
                    print("o=", 7)
                    list.remove(7)
                    list.insert(7, 'o')
                if list[9]!='x' and list[9]!='o':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9, 'o')
            if a==8:
                list.remove(a)
                list.insert(a,'x')
                if list[1]!='x' and list[1]!='o':
                    print("o=",1)
                    list.remove(1)
                    list.insert(1,'o')
                if list[3]!='x' and list[3]!='o':
                    print("o=",3)
                    list.remove(3)
                    list.insert(3, 'o')
                if list[7] != 'x' and list[7] != 'o':
                    print("o=", 7)
                    list.remove(7)
                    list.insert(7, 'o')
                if list[9]!='x' and list[9]!='o':
                    print("o=",9)
                    list.remove(9)
                    list.insert(9, 'o')
            print(list)
        if list[5]=='x':
            if a==2:
                list.remove(a)
                list.insert(a,'x')
                print(list)
