class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def DFS(node, currNum):
            if node:
                if not node.left and not node.right: # leaf
                    return currNum*10 + node.val
                sum = 0
                sum += DFS(node.left, currNum*10+node.val)
                sum += DFS(node.right, currNum*10+node.val)
                return sum
            else:
                return 0


        return DFS(root, 0)