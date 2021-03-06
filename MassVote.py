def MassVote(N,Votes):
    s1 = 'majority winner'
    s2 = 'minority winner'
    s3 = 'no winner'
    sortVotes = sorted(Votes, reverse = True)
    maxVotes = sortVotes[0]
    if sortVotes[0] == sortVotes[1]: return s3
    resultVotes = round((sortVotes[0] * 100 / sum(Votes)),3) 
    for i in range(N):
        if Votes[i] == sortVotes[0]: position = ' ' + str(i+1)
    if resultVotes > 50: return s1 + position
    else: return s2 + position
