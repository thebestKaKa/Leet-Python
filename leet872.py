# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getSeq(root1) == self.getSeq(root2)

    def getSeq(self, root: TreeNode):
        res = []

        def dfs(temp: TreeNode):
            if temp.left is None and temp.right is None:
                res.append(temp.val)
            if temp.left:
                leftchild = temp.left
                dfs(leftchild)
            if temp.right:
                rightchild = temp.right
                dfs(rightchild)

        dfs(root)
        return res


if __name__ == '__main__':
    t4 = TreeNode(6)
    t6 = TreeNode(9)
    t7 = TreeNode(8)
    t8 = TreeNode(7)
    t9 = TreeNode(4)
    t5 = TreeNode(2, left=t8, right=t9)
    t2 = TreeNode(5, left=t4, right=t5)
    t3 = TreeNode(1, left=t6, right=t7)
    t1 = TreeNode(3, left=t2, right=t3)  # root
    s = Solution()
    ans = s.getSeq(t1)
    print(ans)
    print(s.leafSimilar(t1,t1))
