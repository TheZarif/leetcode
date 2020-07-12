class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen={}
        
        def visit(i,j,q,q2):
            nonlocal board
            nonlocal seen
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return 1
            if board[i][j]=="X":
                return 0
            if (i,j) not in seen:
                seen[(i,j)]=True
                q.append((i,j))            
                q2.append((i,j))
            return 0

        
        def dfs(i,j):
            nonlocal board
            q=[(i,j)]
            q2=[(i,j)]
            surrounded=True
            seen[(i,j)]=True
            while len(q)>0:
                (i,j)=q.pop()
                a=visit(i+1,j,q,q2)
                b=visit(i-1,j,q,q2)
                c=visit(i,j+1,q,q2)
                d=visit(i,j-1,q,q2)
                if a+b+c+d>0:
                    surrounded=False
            if surrounded:
                for (x,y) in q2:
                    board[x][y]='X'
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='O' and (i,j) not in seen:
                    dfs(i,j)
