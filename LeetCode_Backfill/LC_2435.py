class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(m):
            for j in range(n):
                current_val = grid[i][j]
                
                for r in range(k):
                    
                    if i == 0 and j == 0:
                        continue
                    
                    r_prev = (r - current_val % k + k) % k
                    
                    if i > 0:
                        dp[i][j][r] = (dp[i][j][r] + dp[i-1][j][r_prev]) % MOD
                        
                    if j > 0:
                        dp[i][j][r] = (dp[i][j][r] + dp[i][j-1][r_prev]) % MOD

        return dp[m-1][n-1][0]