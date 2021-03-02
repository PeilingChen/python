# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:29:31 2021

@author: user

(挑戰題)印出
   *   
  ***  
 ***** 
*******
 ***** 
  ***  
   *   

"""

for i in range(1,9,2):
	for a in range((7-i)//2):
		print(" ",end = '')
	for b in range(i):
		print("*",end = '')
	for a in range((7-i)//2):
		print(" ",end = '')
	print()
	
for i in range(5,0,-2):
	for a in range((7-i)//2):
		print(" ",end = '')
	for b in range(i):
		print("*",end = '')
	for a in range((7-i)//2):
		print(" ",end = '')
	print()

print("程式執行完畢")