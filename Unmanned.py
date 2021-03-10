def Unmanned(L, N, track):
    time = 0
    position = 1
    z = 0    
    for i in range(position,L+1,1):
        time += 1
        if z < N and i == track[z][0]:
            position = i + 1
            per = 0
            while per < time:
                for j in range(1,3,1):       
                    per += track[z][j]
                    if per >= time: break 
            if j == 1: time += per - time
            z += 1
    return time
