# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:20:25 2021

@author: user
作業一:2/1 + 3/2 + 5/3 + 8/5 + ...共20項 =
    
"""

a = 1
b = 2
sum = 0

for i in range(20):
    temp = a
    a = b
    b = temp + a
    sum += b/a
print(sum)
