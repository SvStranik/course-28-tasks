def stringCopy(string):
    string2 = []
    for i in string:
        per = i[:]
        string2.append(per)
    return string2
def branchAging(string):
    for i in range(len(string)):
        for j in range(len(string[i])):
            string[i][j] = int(string[i][j]) + 1
    return string
def TreeOfLife(H, W, N, tree):
    string = []
    for i in tree:
        i = i.replace('+','1')
        i = i.replace('.','0')
        string.append(list(i))
    counter = 0
    while counter != N:
        string = branchAging(string)
        if counter % 2 != 0:
            string2 = stringCopy(string)
            for i in range(H):
                for j in range(W):
                    if string[i][j] >= 3:
                        string2[i][j] = 0
                        if j - 1 >= 0: string2[i][j-1] = 0
                        if j + 1 < W: string2[i][j+1] = 0
                        if i - 1 >= 0: string2[i-1][j] = 0
                        if i + 1 < H: string2[i+1][j] = 0
            string = string2[:]   
        counter += 1
    resultat =[]
    for i in range(H):
        per = ''
        for j in range(W):
            if string[i][j] == 0: per += '.'
            else: per += '+'
        resultat.append(per)
    return resultat