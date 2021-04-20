def Transform(S,B=''):
    for i in range(len(S)-1):
        for j in range(len(S)-i-1): 
            k = i + j
            if len(S[j:k]) > 0: B += max(S[j:k])
            else: B += S[k]
    return B  


def TransformTransform(A,summa = 0):
    for i in A: S = str(i)
    for j in range(2): S = Transform(S)
    if len(S) == 0: return False
    for s in S: summa += int(s)
    if summa % 2 == 0 : return True
    else: return False
