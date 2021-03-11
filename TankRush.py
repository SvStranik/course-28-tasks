def TankRush(H1, W1, S1, H2, W2, S2):
    s1 = S1.split()
    s2 = S2.split()
    comparison = ''
    for i in s2:
        for j in s1:
            entry = False
            if (j in comparison) != True and i in j:
                comparison += j + ' '
                entry = True
                break
        if entry == False: return entry
    return entry
