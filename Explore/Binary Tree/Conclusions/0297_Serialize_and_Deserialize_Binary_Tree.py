# Problem 297
# Date: 2019/09/08

# 132 ms
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        arr = []
        queue = [[root,0]]
        n = 1

        while queue:
            node,ind = queue.pop(0)              
            arr.append([node.val])
            if node.left:
                queue.append([node.left,len(queue)])
                arr[-1].append(n)
                n += 1
            elif node.right:
                arr[-1].append(None)

            if node.right:
                queue.append([node.right,len(queue)])
                arr[-1].append(n)
                n += 1

        return str(arr)
                                                   
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '': return None
        
        arr = [[int(a) if 'None' not in a else None for a in d.split(',')] for d in data[2:-2].replace('[','], ').split('], ') if d != '' ]
        
        nodes = [TreeNode(a[0]) for a in arr]
        
        for i in range(len(arr)):
            a = arr[i]
            if len(a) > 1 and a[1]: nodes[i].left = nodes[a[1]]
            if len(a) > 2: nodes[i].right = nodes[a[2]]      
        return nodes[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
