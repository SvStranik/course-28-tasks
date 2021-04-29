def BalancedParentheses(N):
    if N == 1: return '()'
    if N == 2: return '(()) ()()'
    per = BalancedParentheses(N-1).split()
    per2 = []
    for i in per:
        if i[0] + '()' + i[1:] not in per2:
            per2.append(i[0] + '()' + i[1:])
        if i[:2] + '()' + i[2:] not in per2:
            per2.append(i[:2] + '()' + i[2:])
        if '()' + i not in per2: 
            per2.append('()' + i)
    N = ' '.join(per2)
    return N
