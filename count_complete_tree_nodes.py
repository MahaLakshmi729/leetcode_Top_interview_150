class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        left=right=root
        h_l=h_r=0
        while left:
            h_l+=1
            left=left.left
        while right:
            h_r+=1
            right=right.right
        if h_l==h_r:
            return (1<<h_l)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)        