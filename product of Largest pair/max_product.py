def max_product(a):
    for i in range(1, max(a)):
        b = (max(a)-1) - i
        if b not in a:
             break
    return max(a) * b


print(max_product([56, 335, 195, 443, 6, 494, 252]))
