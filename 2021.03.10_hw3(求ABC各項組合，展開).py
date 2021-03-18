# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 02:25:48 2021

@author: user
作業三: 求ABC各項組合，展開

"""

list = ["A","B","C"]
newlist =[]

temp = 0

for i in range(len(list)):
    if len(list) == 2:
        list.insert(0,temp)
        newlist.clear()
    newlist.append(list[i])
    temp = list[i]
    del list[i]
    newlist.append(list[0])
    newlist.append(list[1])
    nnlist = "".join(newlist)    #list轉成str
    print(nnlist)
    newlist[1], newlist[2] = newlist[2], newlist[1]
    nnlist = "".join(newlist)    #list轉成str
    print(nnlist)



