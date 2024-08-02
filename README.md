import random

main = int(input("輸入1,2,3,4:"))
aValue = random.randint(1,100)
bValue = []
math = 0
n= 0
d = 0

for i in range(1,aValue+1):
    if aValue % i == 0 :
        bValue.append(i)
        n = n + 1
    
math = random.randint(0,n - 1)
d = bValue[math]
print(bValue)


print("數字1=",aValue,"數字2=",d)

if main == 1:
    answer = aValue + d
    print(answer)

elif main == 2:
    answer = aValue - d
    print(answer)
    
elif main == 3:
    answer = aValue * d
    print(answer)
    
elif main == 4:
    answer = aValue / d
    print(answer)
