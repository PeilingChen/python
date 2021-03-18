# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:32:48 2021

@author: user
作業一:有四個數字：1,2,3,4 ，能組成多少個互不相同的，且無重複數字的三位數？各是多少？

"""

def fac(n):       #!的函式
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)
    
def com(n,m):
    return fac(n)/fac(n-m) #排列組合公式

print("能組成%d種三位數"%(com(4,3)))
print("分別為:")

list = [1,2,3,4]
newlist =[]
temp = 0

for a in range(len(list)):
    newlist.append(list[a])
    for b in range(len(list)):
        if list[b] == newlist[0]:
            continue
        newlist.append(list[b])
        for c in range(len(list)):
            if list[c] == newlist[0] or list[c] == newlist[1]:
                continue
            newlist.append(list[c])
            print(newlist[0],newlist[1],newlist[2], sep = '')
            del newlist[2]
        del newlist[1]
    del newlist[0]

    