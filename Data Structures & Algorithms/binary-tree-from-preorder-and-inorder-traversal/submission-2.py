# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_dic = {}
        for i in range(len(inorder)):
            self.inorder_dic[inorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return
        
        root_val = preorder[pre_start]
        root_inorder_idx = self.inorder_dic[root_val]
        left_length = root_inorder_idx - in_start

        root = TreeNode(root_val)
        root.left = self.build(preorder, pre_start + 1, pre_start + left_length, inorder, in_start, in_start+left_length)
        root.right = self.build(preorder, pre_start + left_length + 1, pre_end, inorder, root_inorder_idx + 1, in_end)
        return root