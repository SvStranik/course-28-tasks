def MaximumDiscount(N,price):
    priceMax = sorted(price, reverse = True)
    diskount = 0
    for i in range(N):
        if (i+1) % 3 == 0: diskount += priceMax[i]
    return diskount
