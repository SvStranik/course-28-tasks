def shiftDoor(doors,n):
    for i in range(n-1,len(doors),n):
        if doors[i] == '0': doors[i] = '1'
        else: doors[i] = '0'
    return doors
def Keymaker(k,n=2):
    if k == 1: return '1' 
    doors = ['1'] * k
    while n < k:
        shiftDoor(doors,n)
        n +=1
    else:
        if doors[k-1] == '0': doors[k-1] = '1'
        else: doors[k-1] = '0'
    return ''.join(doors)
