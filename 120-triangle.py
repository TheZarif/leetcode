class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n))
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==0:
            return 0
        row=[]
        
        for i in range(len(triangle)):
            row2=[]
            for j in range(len(triangle[i])):
                if i==0:
                    row2.append(triangle[i][j])
                elif j==0:
                    row2.append(row[j]+triangle[i][j])
                elif j==len(triangle[i])-1:
                    row2.append(row[j-1]+triangle[i][j])
                else:
                    row2.append(min(row[j],row[j-1])+triangle[i][j])
            row=row2
        return min(row)
