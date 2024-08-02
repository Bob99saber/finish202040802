# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:11:18 2024

@author: User
"""

import random

main = int(input("輸入1,2,3,4:"))
aValue = random.randint(1,100)
bValue = 0

for i in range(2,aValue):
    if aValue % i == 0:
        bValue = i
        break

print("數字1=",aValue,"數字2=",bValue)

if main == 1:
    answer = aValue + bValue
    print(answer)

elif main == 2:
    answer = aValue - bValue
    print(answer)
    
elif main == 3:
    answer = aValue * bValue
    print(answer)
    
elif main == 4:
    answer = aValue / bValue
    print(answer)
    
    
