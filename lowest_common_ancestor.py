__author__ = 'baidu'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        pvalue, qvalue = sorted([p.val, q.val])
        lca = root
        while lca!=None:
            if lca.val >= pvalue and lca.val <= qvalue:
                return lca
            if lca.val < pvalue :
                lca = lca.right
            if lca.val > qvalue:
                lca = lca.left
        return None