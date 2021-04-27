def BalancedParentheses(N):
    if N == 1: return '()'
    if N == 2: return '(()) ()()'
    per = BalancedParentheses(N-1).split()
    per.append(per[0])
    per[0] = '(' + per[0] + ')'
    for i in range(1,len(per)):
        per[i] = per[i] + '()'
    N = ' '.join(per)
    return N
