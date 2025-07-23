from typing import List

class Solution: 
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # transposing the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reflection

        for i in range(n):
            for j in range(n // 2):
                ( matrix[i][j], matrix[i][n - j - 1] ) = ( matrix[i][n - j - 1], matrix[i][j] )

matrix = [[1, 2, 3, 10],
          [4, 5, 6, 20],
          [7, 8, 9, 30],
          [11, 12, 13, 40]]

Solution().rotate(matrix)

for row in matrix:
    print(row)
