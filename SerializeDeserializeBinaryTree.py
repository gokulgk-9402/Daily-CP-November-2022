# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """        
        vals = []

        def helper(node):
            if not node:
                vals.append("N")
                return
            
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        return " ".join(vals)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())

        def helper():
            v = next(vals)
            if v == "N":
                return None
            node = TreeNode(int(v))
            node.left = helper()
            node.right = helper()
            return node

        return helper()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))