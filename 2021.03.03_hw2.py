# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:36:33 2021

@author: user

作業二:1A2B

"""
#我的方法:四位數的ans切成wxyz四個數字，input則用個十百千來run。



#一、設定變數(讓wxyz皆隨機，且wxyz彼此間!=)
w = 0
x = 0
y = 0
z = 0   #設定0，使其進入while迴圈
      
while w == x or w == y or w == z or x == y or x == z or y == z:
#因為不知道要random幾次才會讓wxyz彼此間!=，所以用loop
    import random     #在while裡import，如果在While之前先import，就不是在while裡了
    w = random.randint(1,9)
    x = random.randint(1,9)
    y = random.randint(1,9)
    z = random.randint(1,9)

guess = 0

count_a = count_b = 0




#二、while loop2(計算幾a幾b)
#if(use 1000,100,10,//,%)，是否有更簡單的方法，來判定input的位數？
#答對也會跑出猜錯？ -->記得break

while guess//1000 != w or guess // 100 % 10 != x or guess // 10 % 10 != y or guess % 10 != z:
#while要寫!=，才能進入迴圈
#因為是!=，所以用or
#以下在同個迴圈
    guess = int(input("請輸入四位數\n(且每位數字不可重複，不為0):"))   
    #若可以為0?

    if guess // 1000 < 1 or guess // 1000 > 9:   # 排除input不為四位數
    # if guess // 1000 < 1 or guess // 1000 > 9 or guess//1000 == guess//100%10 or guess//1000 == guess//10%10 or guess//1000 == guess%10 or guess//100%10 == guess//10%10 or guess//100%10 == guess%10 ==  or guess//10%10 == guess%10:
    # 嘗試要阻擋重複數字的input，但失敗
        print("輸入錯誤!")
        continue               #continue讓後面xAxB先不要跑出來
    
    if guess//1000 == w:
        count_a = 1
    else:
        count_a = 0             #第一次count_a=1  else:count=0，
    
    if guess//100%10 == x:
        count_a += 1
    else:
        count_a += 0            #第二次之後count_a都要 +=1、+=0
        
    if guess//10%10 == y:
        count_a += 1
    else:
        count_a += 0
    
    if guess%10 == z:
        count_a += 1
    else:
        count_a += 0

    
    if guess//1000 == w or guess // 1000 == x or guess // 1000 == y or guess // 1000 == z:
        count_b = +1
    else:
        count_b = +0
    
    if guess//100%10 == w or guess // 100 % 10 == x or guess // 100 % 10 == y or guess // 100 % 10 == z:
        count_b += 1
    else:
        count_b += 0
        
    if guess//10%10 == w or guess // 10 % 10 == x or guess // 10 % 10 == y or guess // 10 % 10 == z:
        count_b += 1
    else:
        count_b += 0
    
    if guess%10 == w or guess % 10 == x or guess % 10 == y or guess % 10 == z:
        count_b += 1
    else:
        count_b += 0
    
    if guess//1000 == w and guess // 100 % 10 == x and guess // 10 % 10 == y and guess % 10 == z:
        break
    #加這行才能讓最後猜對時，不再顯示"4A4B"，而是直接跳出迴圈，顯示"答對"
    print(count_a, "A", count_b, "B", sep = '')

print("恭喜答對!")

