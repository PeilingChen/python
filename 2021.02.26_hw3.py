# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:28:41 2021

@author: user

作業三:由使用者輸入數值，請透過for要1~數值做加總，最後印出總額。
    
"""

value = int(input("請輸入數值:"))
total = 0

for i in range(1,value+1):
	total += i
print(total)

print("程式執行完畢")