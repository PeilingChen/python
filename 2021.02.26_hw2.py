# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:29:32 2021

@author: user

作業二:用for迴圈，印出
123456789
12345678
1234567
123456
12345
1234
123
12
1

"""

for i in range(9,0,-1):
	for i in range(1,i+1):
		print(i, end = '')
	print()

print("程式執行完畢")