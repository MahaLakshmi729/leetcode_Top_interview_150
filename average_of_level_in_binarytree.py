class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = deque()                    
        level = count = 0                   
        row_avg = [0]                       
        nodes.appendleft(root)
        nodes.appendleft(None)              
        while nodes:

            node = nodes.pop()
            if node:

                count += 1
                row_avg[level] += node.val
                
                if node.left:
                    nodes.appendleft(node.left)
                if node.right:
                    nodes.appendleft(node.right)
            else:                           
                row_avg[level] /= count     
                if nodes:                   
                    nodes.appendleft(None)
                    level += 1
                    row_avg.append(0)       
                    count = 0
        return row_avg