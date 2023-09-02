def count_integer_pairs(a, b, c):
    dp = [[0] * (c+1) for _ in range(c+1)]
    dp[0][0] = 1

    for x in range(c+1):
        for y in range(c+1):
            if a*x + b*y <= c:
                dp[x][y] = 1

    for x in range(1, c+1):
        for y in range(c+1):
            if y > 0:
                dp[x][y] += dp[x-1][y-1]
            dp[x][y] += dp[x-1][y]

    return dp[c][c]

print(count_integer_pairs(10,5,20))