# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:41:00 2021

@author: user
作業七:因數分解
    
"""

x = int(input("欲做因式分解，請輸入正整數:"))

list = []
def prime(n):
    # 確認2~n的質數(可能是n的因數，可能不是)
    # 用for loop找出，並放到list備用
    for a in range(2,n+1):
        p = 0
        for b in range(2,a):
            if a % b == 0:
                p = 1
                break
        if p == 0:
            list.append(a)  

list_f = []    
def factor(n):
    # 找出x的因數(從質數list找)
    prime(n)    
    for c in list:
        if n % c == 0:
            list_f.append(c)
            del list[0:(len(list))]
            return factor(n//c)     #為何要使用//?
    
def final(x):
    #list中各項int轉成str
    factor(x)
    for y in range(0,len(list_f)):
        list_f[y] = str(list_f[y])  
    str_list_f = " * ".join(list_f)    #list轉成str
    print(x, "= {}".format(str_list_f))

final(x)
