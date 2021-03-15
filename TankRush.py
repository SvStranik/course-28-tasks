def TankRush(H1, W1, S1, H2, W2, S2):
    equal = False
    for i in range(len(S1)-W1):
        counter = i
        equal = True
        for j in range(len(S2)):
            if S2[j] == ' ':
                counter = counter + W1 - j + 1
                continue
            if S1[counter] == S2[j]:counter += 1
            else:
                equal = False
                break            
        if equal: return equal
    return equal
