# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxsum=root.val
        parents={}
        parents[root]=None
        nodelist=[]
        def recTraverse(node: TreeNode):
            nonlocal nodelist
            nonlocal parents
            
            nodelist.append(node)
            if node.left:
                parents[node.left]=node
                recTraverse(node.left)
            if node.right:
                parents[node.right]=node
                recTraverse(node.right)
            return
        
        recTraverse(root)
        
        def recPathSum(node, s, isOrigin=False):
            nonlocal seen
            if node is None:
                return 0
            if node in seen:
                return 0
            seen[node]=True
            p=recPathSum(parents[node],s)
            l=recPathSum(node.left, s)
            r=recPathSum(node.right, s)
            if s:
                s+=node.val
            else:
                s=node.val
            if isOrigin:
                s=max(s+p+l,s+p+r,s+l+r,s+p,s+r,s+l,s)
            else:
                s=max(s+p,s+l,s+r,s)
            return s
        
        maxsum=root.val
        for node in nodelist:
            seen={}
            s=recPathSum(node, None, True)
            maxsum=max(maxsum,s)
        return maxsum
