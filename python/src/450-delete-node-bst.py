# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        previous, target = self.search(root, root, key)

        if previous and target:
            self.switch(previous, target)

        return root

    def search(self, previous, current, key):

        if not current:
            return None, None

        if current.val == key:
            return previous, current

        if key < current.val and current.left:

            print(current.val, current.left.val)
            return self.search(current, current.left, key)

        if key > current.val and current.right:
            return self.search(current, current.right, key) 

        return None, None

    def switch(self, previous, target):
        
        if target.right or target.left:

            if target.right:
                if previous.left.val == target.val:
                    node = previous.left
                    previous.left = target.right
                    previous.left.left = node
                if previous.right.val == target.val:
                    node = previous.right
                    previous.right = target.right
                    previous.right.left = node
            else:
                if target.left:
                    node = previous.left
                    previous.left = target.left
        else:
            if previous.left.val == target.val:
                previous.left = None
            if previous.right.val == target.val:
                previous.right = None
            