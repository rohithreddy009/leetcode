class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0

        for c in s:
            if c == "(":
                res.append(c)
                count += 1
            elif c == ")" and count > 0:
                res.append(c)
                count -= 1
            elif c != "(" and c != ")":
                res.append(c)
            
        filtered = []
        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)

        return "".join(filtered[::-1])

# constant space solution
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        chars = list(s)
        n = len(chars)

        # getting rid of extra ")"
        for i in range(n):
            if chars[i] == '(':
                count += 1
            elif chars[i] == ')':
                if count == 0:
                    chars[i] = ''
                else:
                    count -= 1
            
        
        # ignoring "(" and appending to the solution
        for i in range(n-1, -1, -1):
            if chars[i] == '(' and count > 0:
                chars[i] = ''
                count -= 1
        
        return ''.join(chars)

print(Solution().minRemoveToMakeValid("lee(t(c)o)de)(("))  # "lee(t(c)o)de"
print(Solution().minRemoveToMakeValid("()x(("))  # "lee(t(c)o)de"