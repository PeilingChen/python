# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:40:43 2021

@author: user

作業一:
    ans → 80
    guess = 60
    請輸入61~100之間值
    guess = 95
    請輸入61~94之間值


"""
import random
ans = random.randint(1,100)
guess = 0

min = 1
max = 100  #直接設定(因為範圍在1~100)

while ans != guess:
    guess = int(input("請輸入1~100之間的數字:"))
    #"1~100"一直跑出來......
    #無法使用guess = int(input("請輸入",min,"~",max,"之間的數字" , sep = '' )?
    if ans ==guess:
        break
    #使答對時，可以從loop跳出來，避免出現例如min==76,max==79 ,guess==ans==78 --> "請輸入1~100之間的數字:" 才顯示 "恭喜答對"
    if min <= ans <= guess:
    #1和100直接用min和max來代數(因為迴圈後會改變，就不是1和100)
    #有可能==1或==100，所以使用<=
        max = guess-1
        print("請輸入",min,"~",max,"之間的數字" , sep = '' )
    elif guess <= ans <= max:
        min = guess + 1
        print("請輸入",min,"~",max,"之間的數字" , sep = '' )

print("恭喜答對!")
