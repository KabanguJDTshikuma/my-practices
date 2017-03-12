def max_sumDig(nMax, maxSum):
    satisfy = 0
    #meanFound = 0
    sumAll = 0
    data = list()
    minim = list()
    for i in range(1000, nMax+1):
    #for i, dig in list(zip(range(1000, nMax+1),list(str(i)))):
        add = 0
        #add += int(dig)
        for dig in list(str(i)):
            add += int(dig)
        if add <= maxSum: #or add == maxSum:
            satisfy += 1
            minim.append(i)
            sumAll += i

    meanFound = int(sumAll/satisfy)
    if meanFound not in minim:
        minim.append(meanFound)
        minim.sort()
        data.append(satisfy)
        a = meanFound - (minim[minim.index(meanFound) - 1])
        b = (minim[minim.index(meanFound) + 1]) - meanFound
        if a < b:
            data.append(minim[minim.index(meanFound) - 1])
        else:
            data.append(minim[minim.index(meanFound) + 1])
        data.append(sumAll)
        return data
    else:
        data.append(satisfy)
        data.append(meanFound)
        data.append(sumAll)
        return data


print(max_sumDig(2000, 7))






