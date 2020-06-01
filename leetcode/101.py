class Solution:
    def isSymmetric(self, root) -> bool:
        if not root: return True
        return self.isSTree(root.left,root.right)
    #     global r
    #     r =  []
    #     f = 0
    #     self.mid(root, f)
    #     print(r)
    #     if r == r[::-1]:
    #         return True

    # def mid(self, root, f):
    #     f += 1
    #     if root == None:
    #         r.append(f)
    #     else:
    #         self.mid(root.left, f)
    #         r.append(root.val)
    #         self.mid(root.right, f)

    def isSTree(self,left,right):
        if left is None and right is None: return True
        if left is None or right is None: return False
        if left.val != right.val: return False
        return self.isSTree(left.left,right.right) and self.isSTree(left.right, right.left)