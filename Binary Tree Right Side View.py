class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if node:
                if depth == len(ans):
                    ans.append(node.val)
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        ans = []
        dfs(root, 0)
        return ans



        