# recursive divide and conquer approach
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = helper(x, n//2)
            res = res * res
            return res * x if n%2 == 1 else res
        
        soln = helper(x, abs(n))
        return soln if n > 0 else 1/soln

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        result = 1.0
        current_product = x

        while N > 0:
            if N % 2 == 1:
                result *= current_product
            current_product *= current_product
            N //= 2

        return result if n >= 0 else 1 / result


print(Solution2().myPow(2.00000, 10))  # Output: 1024.00000
print(Solution().myPow(2.10000, 3))   # Output: 9.26100
print(Solution().myPow(2.00000, -2))  # Output: 0.25000