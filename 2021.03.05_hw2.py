# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:28:06 2021

@author: user

作業二:大樂透(1~49之間亂數取6個不重複數字，並印出)
問題1: 是否可用while迴圈? (遇到跟前面重複的continue，然後如何跳出迴圈?)
問題2: 若用"複製串列"的方式? .append(i)還能隨機嗎?
"""



lottery = list(range(0,50))    #將1~49的數字變成串列

import random
num_1 = random.randint(1,50)  
print(lottery[num_1:num_1+1])
del lottery[num_1:num_1+1]     #刪除串列中已取出的數，避免後面重複

num_2 = random.randint(1,49)
print(lottery[num_2:num_2+1])
del lottery[num_2:num_2+1]

num_3 = random.randint(1,48)
print(lottery[num_3:num_3+1])
del lottery[num_3:num_3+1]

num_4 = random.randint(1,47)
print(lottery[num_4:num_4+1])
del lottery[num_4:num_4+1]

num_5 = random.randint(1,46)
print(lottery[num_5:num_5+1])
del lottery[num_5:num_5+1]

num_6 = random.randint(1,45)
print(lottery[num_6:num_6+1])
del lottery[num_6:num_6+1]
