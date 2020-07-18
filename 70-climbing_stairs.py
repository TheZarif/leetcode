class Solution:
# Complexity: O(n)
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        n1=0
        n2=1
        for i in range(n):
            t=n1+n2
            n1=n2
            n2=t
        return t
