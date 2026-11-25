class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)
        # dp[i][j] = min operations to convert word1[:i] to word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i             # i zdeletes
        for j in range(n + 1):
            dp[0][j] = j             # j inserts

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],   # replace
                                    dp[i - 1][j],       # delete
                                    dp[i][j - 1])       # insert
        return dp[m][n] 
