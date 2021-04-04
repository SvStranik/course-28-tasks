def BiggerGreater(string):
    for i in range(len(string)-1,0,-1):
        if string[i] > string[i-1]:
            string2 = list(string[i-1:])
            stringMax = sorted(string2)
            element = stringMax[stringMax.index(string2[0])+1]
            x = string2.index(element)
            string2[0],string2[x] = string2[x],string2[0]
            string = string[:i-1] + ''.join(string2[0]) + ''.join(sorted(string2[1:]))
            return string    
    string = ''      
    return string