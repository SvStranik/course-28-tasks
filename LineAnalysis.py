def LineAnalysis(line):
    bool = False
    symbol = '*'
    if line == symbol * len(line): 
        bool = True
        return bool
    if line[0] != symbol or line[len(line)-1] != symbol:
        return bool
    convertedLine = line[1:len(line)-1]
    convertedLine1 = (convertedLine.replace('*',',')).split(',')
    for i in range(len(convertedLine1)-1):
        if convertedLine1[i] != convertedLine1[i+1]: return bool
    bool = True
    return bool
