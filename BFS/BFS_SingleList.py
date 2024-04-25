# leetcode 102 binary tree order traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using dummyNode to achieve

class Solution:
    def BFS_single(root):
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        while queue:
            res.append([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res