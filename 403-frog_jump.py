class Solution:
    # Complexity: Time O(nk), Space O(n,k)
    
    def canCross(self, stones: List[int]) -> bool:
        dp={}
        def recCross(i, k):
            nonlocal stones
            nonlocal dp
            if (i,k) in dp:
                return dp[(i,k)]
            if k==0:
                return False
            if stones[-1]==i+k:
                return True
            if i+k in stones:                
                dp[(i,k)] = recCross(i+k,k+1) or recCross(i+k,k) or recCross(i+k,k-1)
            else:
                dp[(i,k)]= False
            return dp[(i,k)]
        return recCross(0,1)
