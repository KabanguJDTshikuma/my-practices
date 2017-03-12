def sum_of_n(n):
    a = 0
    b = []
    if n < 0:
        n = abs(n)
        for i in range(n+1):
            a += i
            b.append(-a)
        return b
    else:
        for i in range(n+1):
            a += i
            b.append(a)
        return b
        

print(sum_of_n(7))
        
        
