def recreation_one(m, n):
    import math
    divisor = []
    #sublist = []
    #some = 0
    for integer in range(m, (n+1)):
        sublist = []
        some = 0
        if integer == 1:
            sublist.append(1)
            sublist.append(1)
        else:
            for i in range(1, (integer+1)):
                div = integer%i
                if div == 0:
                    some += i
            sublist.append(integer)
            sublist.append(some)
                #print(sublist)
        divisor.append(sublist)
    print(divisor)
    #return(divisor)
(recreation_one(1,45))











