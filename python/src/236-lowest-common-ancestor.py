# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    found_p = False
    found_q = False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.pre_order(root, p, q)

    def pre_order(self, current, p, q):
        if not current:
            return None

        # visit current
        if current.val == p.val:
            self.found_p = True
            if self.found_q:
                return q
        if current.val == q.val:
            self.found_q = True
            if self.found_p:
                return p

        result = self.pre_order(current.left, p, q)
        if result:
            return result

        if current.left:
            if self.found_p:
                if self.find(current.left, p):
                    p = current

            if self.found_q:
                if self.find(current.left, q):
                    q = current

        return self.pre_order(current.right, p, q)

    def find(self, node, target):
        if not node:
            return False
        if node.val == target.val:
            return True
        if self.find(node.left, target) or self.find(node.right, target):
            return True
        return False