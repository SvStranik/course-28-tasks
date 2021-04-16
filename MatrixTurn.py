def rotationMatrix(matrix,M,N):
    counter, resultat,counter2 = 1,[],0
    for i in range(M):
        per = ''
        if i+1 < M: per = matrix[i+1][:counter]
        per +=matrix[i][counter2:N-counter]
        if i > 0:per += matrix[i-1][N-counter2:] 
        resultat.append(per)
        if i >= M - N //2 and i+1 > M // 2:counter2 -= 1
        if counter2 < N // 2 and  i+1 <= M // 2: counter2 += 1
        if i+1 >= M - N //2 and i+1 >= M // 2:counter -= 1
        if counter < N // 2 and  i+1 < M // 2: counter += 1   
    return resultat
def MatrixTurn(matrix,M,N,T):
    global Matrix
    for j in range(T):
        matrix = rotationMatrix(matrix,M,N)
        Matrix = matrix[:]