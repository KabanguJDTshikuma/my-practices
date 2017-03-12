def dirReduc(arr):
    d = 0
    for i in arr:
        d = d + 1
        s = i + arr[d]
        if s == 'NORTHSOUTH' or 'SOUTHNORTH':
            arr.remove(i)
            arr.remove(arr[d-1])
        elif s == 'EASTWEST' or 'WESTEAST':
            arr.remove(i)
            arr.remove(arr[d-1])
        elif s == 'NORTHWEST' or 'WESTNORTH':
            continue
        elif s == 'WESTSOUTH' or 'SOUTHWEST':
            continue
        elif s == 'SOUTHEAST' or 'EASTSOUTH':
            continue
        elif s == 'EASTNORTH' or 'NORTHEAST':
            continue
        elif s == 'EASTEAST' or 'WESTWEST' or 'SOUTHSOUTH' or 'NORTHNORTH':
            arr.remove(arr[i])
        elif d == len(arr):
            break
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
            
        
