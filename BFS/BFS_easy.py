# leetcode 102 binary tree order traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using dummyNode to achieve
class Solution(object):
    def levelOrder_collection_deque(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #using queue to store the root node
        queue = collections.deque([root])
        #base case check if ROOT is empty or not
        if not root:
            return []
        
        results = []
        while queue:
            results.append([node.val for node in queue])
            for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return results
            

# using double list to achieve 
    def levelOrder_doublelist_doublelist(self, root):
        queue = [root]
        if not root:
            return []
        
        results = []
        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                queue = next_queue
                
        return results
    
    def levelOrder_dummynode(self, root):
        if not root:
            return []
        
        queue = collections.deque([root, None])
        result, level = [], []
        
        while queue:
            node = queue.popleft()
            if node is None:
                result.append(level)
                level = []
                if queue:
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
    
        return result    
            
            
        
        
                    
                
            
        
        