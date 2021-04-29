def BalancedParentheses(N):
    a = 0
    variants = []
    if N > 0:
        variant = ['(', 1, 1]
        variants.append(variant)
        while a == 0:
            a = 1
            for v in variants:
                if v[1] < N and v[2] > 0:
                    a = 0
                    variants.append([v[0] + ')', v[1], v[2] - 1])
                    v[0] += '('
                    v[1] += 1
                    v[2] += 1
                elif v[1] == N and v[2] > 0:
                    a = 0
                    v[0] += ')'
                    v[2] -= 1
                elif v[1] < N and v[2] == 0:
                    a = 0
                    v[0] += '('
                    v[1] += 1
                    v[2] += 1
    else:
        return []
    for i in variants:
        variants[variants.index(i)] = i[0]
    return ' '.join(variants)
    