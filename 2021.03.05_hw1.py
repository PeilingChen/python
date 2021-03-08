# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:32:03 2021

@author: user

作業一:氣泡排序法bubble sort
"""
#提示:巢狀迴圈
#提示: number[0]和number[1]比大小，若要交換可使用temp.....

number = list()

while len(number) <= 5:
    num = int(input("請輸入數字:"))
    number.append(num)
    if len(number) == 5:
        break
    
print("串列內容:",number)



while number[0] > number[1]:
    if number[0] > number[1]:
        temp = number[0]
        number[0] = number[1]
        number[1] = temp
    while number[1] > number[2]:
        if number[1] > number[2]:
            temp = number[1]
            number[1] = number[2]
            number[2] = temp
        while number[2] > number[3]:
            if number[2] > number[3]:
                temp = number[2]
                number[2] = number[3]
                number[3] = temp
            while number[3] > number[4]:
                if number[3] > number[4]:
                    temp = number[3]
                    number[3] = number[4]
                    number[4] = temp

print("氣泡排序法:", number)        
