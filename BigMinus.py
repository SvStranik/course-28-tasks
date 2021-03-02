def BigMinus(s1,s2):
    if int(s1) < int(s2):
        s1,s2 = s2,s1 
    s2 = s2.rjust(len(s1),'0')

    per = 0
    s = ''
    for i in range(len(s1)-1,-1,-1):
        x = (10 + int(s1[i])- per - int(s2[i])) % 10
        if int(s1[i]) < int(s2[i]) : per = 1
        if int(s1[i]) > int(s2[i]) : per = 0 
        s = str(x) + s
    if s[0] == '0': s = s[1:]
    return s
