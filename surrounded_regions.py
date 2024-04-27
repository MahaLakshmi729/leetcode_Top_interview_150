class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited=set()
        def dfs(x,y):
            if x<0 or x>=len(board) or y<0 or y>=len(board[0]) or board[x][y]=="X" or (x,y) in visited:
                return
            visited.add((x,y))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x,y+1)
        for i in range(len(board)):
            dfs(i,0)
            dfs(i,len(board[0])-1)
        for i in range(len(board[0])):
            dfs(0,i)
            dfs(len(board)-1,i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O" and (i,j) not in visited:
                    board[i][j]="X"
                


