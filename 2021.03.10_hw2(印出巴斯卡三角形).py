# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:29:10 2021

@author: user
作業二: 印出巴斯卡三角形

"""

# 將各行以串列方式產生(方便用和計算新的一行)
def pt(i):
    if i == 1:
        data = [0,1,0]
        return data
    else:
        data = [0]
        for a in range(i,0,-1):
            data.insert(1,pt(i-1)[a-1]+pt(i-1)[a])
        data.insert(i+1, 0)
        return data

#list中各項int轉成str
def ptstr(x):
    data = pt(x)
    for x in range(0,len(data)):
        data[x] = str(data[x])  
    return data

# 從list取出需要的值(頭尾的0不取)
def ptd(b):
    data = ptstr(b)
    del data[0]
    del data[-1]
    strdata = " ".join(data)    #list轉成str(方便後面.center)
    return strdata

p = int(input("請輸入正整數:"))
c = (len(ptd(p)))
for i in range(1,p+1):
    print(ptd(i).center(c))      #無須打print(ptd(i))，否則會印None!




