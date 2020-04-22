"""
// Time Complexity : O(n)
// Space Complexity : O(maxDepth)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
// Your code here along with comments explaining your approach
Algorithm explanation
Level order traversal by using size and keeping track of maximum per level
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        result = []
        while q:
            size = len(q)
            max_val = float("-inf")
            for i in range(size):
                root = q.pop(0)
                max_val = max(max_val,root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            result.append(max_val)
        return result