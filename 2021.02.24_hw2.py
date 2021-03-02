# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:01:30 2021

@author: USER
"""

sum = 0
number = int(input("請輸入次數:"))

for i in range(1,number+1):
    if i % 2 == 0:
        sum += i
print(sum)
