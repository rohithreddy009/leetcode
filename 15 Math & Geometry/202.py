class Solution:
    def isHappy(self, n: int) -> bool:
        visit_set = set()

        def sum_of_squares(n):
            output = 0

            while n != 0:
                digit = n % 10 # get the last digit
                digit = digit * digit  # square it
                output += digit # add to the running total
                n = n // 10 # remove the last digit
            return output

        while n not in visit_set:
            visit_set.add(n)
            n = sum_of_squares(n)

            if n == 1:
                return True

        return False

print(Solution().isHappy(19))  # Example usage 
print(Solution().isHappy(2))   # Example usage