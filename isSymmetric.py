# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left, right):
            if left and right:
                if left.val == right.val:
                    return check(left.left, right.right) and check(left.right, right.left)
                else:
                    return False
            elif left or right:
                return False
            else:
                return True
        if root:
            return check(root.left, root.right)
        else:
            return True