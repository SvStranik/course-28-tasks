def codeEncripted(s):
    S = s.replace(' ','')
    squareRoot = pow(len(S),0.5) 
    if int(squareRoot //1) >= int(squareRoot % 1 * 10):
        string = int(squareRoot % 1 * 10) # Столбец
        column = int(squareRoot //1) # Строка
    else: 
        string = int(squareRoot //1) # Строка
        column = int(squareRoot % 1 * 10) # Столбец
    
    while string * column < len(S):
        string += 1

    arr = []
    count = 0
    for i in range(column):
        arr2 = []
        for j in range(string):
            if count == len(S):break
            arr2.append(S[count])
            count += 1
        arr.append(arr2)

    result = ''
    for i in range(string):
        for j in range(column):
            if i < len(arr[j]):
                result += arr[j][i]
        result += ' '
    result =  result.strip()
    return result
    
def TheRabbitsFoot(s, encode):
    if encode == True:
        return codeEncripted(s)
    else:
        arr = s.split()
        result = ''
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i < len(arr[j]):
                    result += arr[j][i]
        return result
