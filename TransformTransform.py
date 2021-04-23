def Transform(A):
    B = []
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-i-1):
            k = i + j
            B.append(max(A[j:k+1]))
    return B
def TransformTransform(A):
    A = Transform(A)
    B = Transform(A)
    if sum(B) % 2 == 0: return True
    else: return False
