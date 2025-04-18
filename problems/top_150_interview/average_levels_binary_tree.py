# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        q = deque()
        q.append(root)
        print(q)

        while q:
            average = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                average += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            average /= n
            averages.append(average)
        return averages