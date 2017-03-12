def get_sum(a,b):
    sumNum = 0
    if a == b:
        return a 
    elif a > b:
        c = b
        b = a
        a = c
        for i in range(a,b):
            sumNum += i   
        sumNum = sumNum + b
        return sumNum
    else:
        for i in range(a,b):
            sumNum += i   
        sumNum = sumNum + b
        return sumNum

print(get_sum(0,1))
