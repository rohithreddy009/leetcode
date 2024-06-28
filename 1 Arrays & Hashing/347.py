class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for nc in freq[i]:
                res.append(nc)
                if len(res) == k:
                    return res
    

solution = Solution()

print(solution.topKFrequent([3,4,2,3,3], 2))


