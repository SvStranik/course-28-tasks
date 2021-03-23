def sort_key(j):
        return int(j[1])
def ShopOLAP(N,items):
    if N == 1: return items
    Items1 = []
    Items2 = []
    for j in items:
        Items1.append(j.split())
    Items1 = sorted(Items1)
    for i in range(len(Items1)-1):
        if Items1[i][0] == Items1[i+1][0]:
            Items1[i+1][1] = str(int(Items1[i][1]) + int(Items1[i+1][1]))
        else:
            Items2.append(Items1[i])
    Items2.append(Items1[i+1])
    sortItems = sorted(Items2, reverse = True, key=sort_key)
    resultat = []
    for y in range(len(sortItems)):
        per = sortItems[y][0] + ' ' + sortItems[y][1]
        resultat.append(per)
    return resultat
