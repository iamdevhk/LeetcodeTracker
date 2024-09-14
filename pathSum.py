# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        else:
            ans=0
            subSum=sum-root.val
            if subSum==0 and root.left ==None and root.right==None:
                return True
            if root.left is not None:
                ans= ans or self.hasPathSum(root.left,subSum)
            if root.right is not None:
                ans=ans or self.hasPathSum(root.right,subSum)
        return ans


           