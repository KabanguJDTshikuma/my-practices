def longest_collatz(input_array):
    count = 0
    b = []
    c = {}
    for n in input_array:
        a = n
        if a == 1:
            count = 1
        else:
            while a != 1:
                if a % 2 == 0:
                    odd = a/2
                    a = odd
                    odd = 0
                    count += 1
                else:
                    odd = 3 * a + 1
                    a = odd
                    odd = 0
                    count += 1
        c[count] = n
        count = 0
    return c[max(c.keys())]

print(longest_collatz([2, 4, 3]))
