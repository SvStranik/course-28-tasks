def MatrixTurn(Matrix,M,N,T): 
    for j in range(T):
        counter, resultat,counter2 = 1,[],0
        for i in range(M):
            per = ''
            if i+1 < M: 
                per = Matrix[i+1][:counter]
            per +=Matrix[i][counter2:N-counter]
            if i > 0:per += Matrix[i-1][N-counter2:] 
            resultat.append(per)
            if i >= M - N //2 and i+1 > M // 2:counter2 -= 1
            if counter2 < N // 2 and  i+1 <= M // 2: counter2 += 1
            if i+1 >= M - N //2 and i+1 >= M // 2:counter -= 1
            if counter < N // 2 and  i+1 < M // 2: counter += 1   
        Matrix = resultat[:]