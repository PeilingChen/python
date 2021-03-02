# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:41:00 2021

@author: USER
"""

number = int(input("請輸入次數:"))

for i in range(1,number+1):
    if i % 2 != 0:
        print(i)
print("上面數字為奇數")

for i in range(1,number+1):
    if i % 2 == 0:
        print(i)
print("上面數字為偶數")