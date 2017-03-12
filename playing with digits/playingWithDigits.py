def dig_pow(n, p):
    sumN = 0
    for i in str(n):
        sumN += int(i)**p
        p += 1
    if sumN % n == 0:
        k = int(sumN / n)
        return k
    else:
        return -1
print(dig_pow(46288, 3))
