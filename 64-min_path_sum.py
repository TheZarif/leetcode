class Solution:
    # Simply build up DP table taking minimum of left or up item and add to grid item
    # Last item of DP table is the sol
    # Complexity: O(mn)
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[-1][-1]
