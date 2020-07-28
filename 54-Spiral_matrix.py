class Solution:
    # Complexity: Time: O(mn), Space: O(mn)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res=[]
        seen=[[0]*len(matrix[0]) for i in range(len(matrix))]
        if len(matrix)==0 or len(matrix[0])==0:
            return res
        
        def valid(i,j):
            nonlocal seen
            if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
                return False
            if seen[i][j]==1:
                return False
            return True
            
        d=0
        i=0
        j=0
        c=0
        while True:
            if seen[i][j]==1:
                if c>3:
                    break
                c+=1
            else:
                c=0
                seen[i][j]=1
                res.append(matrix[i][j])
            if d%4==0:
                if valid(i,j+1):
                    j+=1
                    continue
            elif d%4==1:
                if valid(i+1,j):
                    i+=1
                    continue
            elif d%4==2:
                if valid(i,j-1):
                    j-=1
                    continue
            elif d%4==3:
                if valid(i-1,j):
                    i-=1
                    continue
            d+=1
        return res
