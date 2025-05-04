# naive recursive solution
class Solution:
    def fib(self, n: int) -> int:
        #base case
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        #recursive case
        return self.fib(n - 1) + self.fib(n - 2)

# memoization ( top dwn approach)
class Solution2:
    def fib(self, n: int) -> int:
        memo = { 0: 0, 1: 1 }
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        
        return f(n)

# bottom up approach
class Solution3:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1


        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]

# constant space solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        curr = 1

        for i in range(2, n+1):
            prev, curr = curr, prev + curr
        
        return curr 
        
        
    
a = Solution2()
print(a.fib(4)) # 3