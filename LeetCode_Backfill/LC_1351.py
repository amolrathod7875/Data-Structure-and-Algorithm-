class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        elements = len(grid[0])
        i = rows - 1
        j = 0
        count = 0
        while i >=0 and j < elements:
            if grid[i][j] < 0:
                count += elements - j
                i -= 1
            else:
                j += 1

        return count