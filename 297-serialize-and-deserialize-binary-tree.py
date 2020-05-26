class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ""
        
        def dfs(node):
            nonlocal result
            if not node:
                result += ("null" + ",")
                return
            result += (str(node.val) + ",")
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        
        def construct(l):
            nonlocal nodes
            val = l.pop(0)
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = construct(l)
            node.right = construct(l)
            return node
        
        root = construct(nodes)
        return root