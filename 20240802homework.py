# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:57:15 2024

@author: User
"""

ListA = [1,1]
math = 0 

n = int(input("輸入運作次數:"))

for i in range(n):
    a = ListA[-1]  # 取列表的最后一个元素
    b = ListA[-2]
    math = a + b
    ListA.append(math)
    

print("輸入",n,"次結果為:",ListA) 
