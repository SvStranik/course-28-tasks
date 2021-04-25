def string1(N):
    if N == 1: return "()"
    return "(" + string1(N-1) + ")"
def string2(N):
    if N == 1: return "("+")"
    return string2(N-1) + "()"
def BalancedParentheses(N):
    if N == 1: return "()"
    S = string2(N)
    N = string1(N)
    return N + S
