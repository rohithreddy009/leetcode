class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string
        dp[1] = 1  # First char is guaranteed not to be '0' (we checked)

        for i in range(2, n + 1):
            # One digit (s[i-1])
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two digits (s[i-2:i])
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

print(Solution().numDecodings("4205"))  # Output: 3