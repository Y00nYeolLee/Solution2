a = input()
flag = 0
result = 0

for i in a :
    i = int(i)
    if i == 0 or i == 1 :
        result += i
        flag = 1
    elif flag == 1 :
        result += i
        flag = 0
    else : 
        result *= i
