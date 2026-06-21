# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use BST 
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = [] #node in the same level
            for i in range(qLen):
                node = q.popleft() # FIFO pop out from queue
                if node:
                    level.append(node.val)
                    q.append(node.left) # append children
                    q.append(node.right)
            if level:
                res.append(level)


        return res