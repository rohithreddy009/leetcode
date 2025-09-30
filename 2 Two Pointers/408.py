class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i, j = i+1, j+1
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            else:
                num = 0
                while j < len(abbr) and not abbr[j].isalpha():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
        
        return True if i == len(word) and j == len(abbr) else False

print(Solution().validWordAbbreviation("internationalization", "i12iz4n"))  # True