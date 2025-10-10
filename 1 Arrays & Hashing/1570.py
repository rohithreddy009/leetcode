from typing import List

# hashmap
class SparseVecto0:
    def __init__(self, nums: List[int]):
        self.hmap = {}
        for i, v in enumerate(nums):
            if v is not 0:
                self.hmap[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, v in vec.hmap.items():
            if i in self.hmap:
                res += v * self.hmap[i]
        return res
    
# tuple using two pointers
class SparseVector:
    def __init__(self, nums: List[int]):
        self.tuple = []
        for i, v in enumerate(nums):
            if v != 0:
                self.tuple.append((i, v))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        i = j = 0

        while i < len(self.tuple) and j < len(vec.tuple):
            i_index, i_val = self.tuple[i]
            j_index, j_val = vec.tuple[j]

            if i_index == j_index:
                dot_product += (i_val * j_val) 
                i += 1
                j += 1
            elif i_index > j_index:
                j += 1
            else:
                i += 1
        
        return dot_product

# Test input
nums1 = [1, 0, 0, 2, 0, 3]  # Non-zero at indices 0, 3, 5
nums2 = [0, 4, 0, 5, 0, 6]  # Non-zero at indices 1, 3, 5

# Create vectors
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)

print("v1.tuple:", v1.tuple)  # Should be: [(0,1), (3,2), (5,3)]
print("v2.tuple:", v2.tuple)  # Should be: [(1,4), (3,5), (5,6)]

# Calculate dot product
result = v1.dotProduct(v2)
print("Dot product:", result)  # Should be: (2*5) + (3*6) = 10 + 18 = 28


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

