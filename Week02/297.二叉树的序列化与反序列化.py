#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#BFS 广度优先
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return
        dq = deque([root])
        seq = []
        while dq:
            node = dq.popleft()
            if node is None:
                seq.append('null') 
                continue
            seq.append(str(node.val))
            dq.extend([node.left, node.right]) 
        return ",".join(seq)      

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        seq = data.split(',')
        root = TreeNode(int(seq[0]))
        dq = deque([root])
        i = 0
        while dq:
            node = dq.popleft()
            i += 1
            if seq[i] != 'null':
                node.left = TreeNode(int(seq[i]))
                dq.append(node.left)
            i += 1
            if seq[i] != 'null':
                node.right = TreeNode(int(seq[i]))
                dq.append(node.right)
        return root
         

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

