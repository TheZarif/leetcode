class Solution:
    #Build up DP table with number of unique paths
    #Complexity: O(mn)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1]==1:
                    dp[i][j]=0
                elif i==1 and j==1:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]
