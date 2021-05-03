def Football(F,N):
    resultat = True
    for i in range(len(F)-1):
        if F[i] > F[i+1] and resultat == True:
            if len(F) - i == 2:
                return True
            elif F[i+1] < F[i+2]:
                for j in range(i+1,len(F)-i):
                    if F[j] > F[j+1]:
                        F[i],F[j+1] = F[j+1],F[i]
                        break
            else:
                for j in range(i+1,len(F)-i):
                    if F[j] < F[j+1]:
                        F[i:j+1] = list(reversed(F[i:j+1]))
                        break
                    if len(F)-i-1 == j:
                        F[i:] = list(reversed(F[i:]))
            resultat = False
        if F[i] > F[i+1] and resultat == False:
            return False
    return True
    