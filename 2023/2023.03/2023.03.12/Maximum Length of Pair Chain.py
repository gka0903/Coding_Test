def findLongestChain(pairs):
    pairs.sort()
    print(pairs)
    dp = [1] * len(pairs)
    for i in range(1, len(pairs)):
        for j in range(i):
            if pairs[i][0] > pairs[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(findLongestChain([[7, 9], [4, 5], [7, 9], [-7, -1], [0, 10], [3, 10], [3, 6], [2, 3]]))
