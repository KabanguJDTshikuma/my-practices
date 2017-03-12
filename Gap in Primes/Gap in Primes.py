def gap(g , m, n):
    val = []
    geo = 0
    for i in range(m, (n+1)):
        for a in range(2, (i-1)):
            if i % a == 0:
                break
        else:
            val.append(i)
        if len(val)== 2:
            geo = val[1]-val[0]
            if geo == g:
                return val
            else:
                del val[0]
print(gap(10,300,400))




