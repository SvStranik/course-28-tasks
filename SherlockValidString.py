def SherlockValidString(s):
    step = 0
    string = sorted(s)
    per1 = string.count(string[0])
    per2 = string.count(string[per1])
    if per1 > per2 and per1-1 == per2:
            per1 = per2
    pos = per1
    bool = True
    while pos < len(string):
        quantityElements = string.count(string[pos])
        if per1 != quantityElements: 
            if (per1 + 1 == quantityElements or quantityElements == 1) and step == 0:
                step = 1
            else:
                bool = False
                return bool
        pos +=quantityElements
    return bool