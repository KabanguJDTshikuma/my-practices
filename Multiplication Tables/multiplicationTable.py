def multiplication_table(row,col):
    y = 0
    z = 1
    T1 = []
    T = []
    for i in range(1, (row+1)):
        while z <= row:
            y += i
            T1.append(y)
            z += 1
        T.append(T1)
        T1 =[]
        z = 1
        y = 0
    return T
print(multiplication_table(4,4))
