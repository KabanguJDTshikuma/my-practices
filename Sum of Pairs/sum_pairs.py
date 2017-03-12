def sum_pairs(ints, s):
    k = 0
    n = 0
    b = list()
    for c, n in enumerate(ints):
        k = c+1
        while k < len(ints):
            n += ints[k]
            if n == s:
                b.append((c, k))
            k += 1


