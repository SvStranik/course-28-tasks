def Transform(A,N):
    B = []
    for i in range(0,N-1):
        for j in range(0,N-i-1):
            k = i + j
            B.append(max(A[j:k+1]))
    return B
def TransformTransform(A,N):
    A = Transform(A,N)
    B = Transform(A,N)
    if sum(B) % 2 == 0: return True
    else: return False
