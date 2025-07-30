class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # Loop while n is not zero
        while n != 0:
            # Check if the last bit is 1
            if n % 2 == 1:
                count += 1
            # Remove the last bit (integer division by 2)
            n = n // 2
        return count

class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n = n & (n - 1)
        
        return res

print(Solution2().hammingWeight(11))  # Example usage