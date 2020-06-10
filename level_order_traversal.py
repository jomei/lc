# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.step(root)
        
    def step(self, node):
        if node == None:
           return []
        result = []
        left = self.step(node.left)
        right = self.step(node.right)
        return [[node.val]] + self.merge(left, right)
    
    def merge(self, l, r):
        result = []
        for i, l_l in enumerate(l):
            if i < len(r):
                result.append(l_l + r[i])
            else:
                result.append(l_l)
                
        if len(r) > len(l):
            for i in range(len(l), len(r)):
                result.append(r[i])
        return result