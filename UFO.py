def UFO(N,data,octal):
    if octal == True: degree = 8
    else: degree = 16
    result = []
    for i in data:
        I = str(i)
        per = len(I)
        summ = 0
        for j in range(len(I)):
            summ = summ + (int(I[j]) * degree ** (per-1))
            per -= 1
        result.append(summ)
    return result
