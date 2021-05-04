def Football(F,N):
    resultat = False
    for i in range(len(F)-1):
        if F[i] > F[i+1] and resultat == False:
            if len(F) - i == 2:
                return True
            elif F[i+1] < F[i+2]:
                counter = i+1
                while F[counter] < F[counter+1]:
                    counter += 1
                    if counter == len(F)-1: 
                        break
                else:
                    F[i],F[counter+1] = F[counter+1],F[i]
            else:
                counter = i
                while counter != len(F)-1 and F[counter] > F[counter+1]:
                        counter += 1
                else:
                    F[i:counter+1] = list(reversed(F[i:counter+1]))                                    
            resultat = True
        if F[i] > F[i+1] and resultat == True:
            return False
    return resultat