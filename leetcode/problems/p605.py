def canPlaceFlowers(bed, n):
    bed = [0] + bed + [0]
    for i in range(1, len(bed)-1):
        if bed[i-1:i+2] == [0,0,0]:
            n -= 1
            bed[i] = 1
    return True if n<=0 else False