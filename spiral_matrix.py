class Solution:
    def spiralOrder(self, arr):
        N = len(arr)
        M = len(arr[0])
        top = 0
        down = N - 1
        left = 0
        right = M - 1
        dir = 0
        ans = []
        while top <= down and left <= right:
            if dir == 0:
                for m in range(left, right + 1):
                    ans.append(arr[top][m])
                top += 1
            elif dir == 1:
                for l in range(top, down + 1):
                    ans.append(arr[l][right])
                right -= 1
            elif dir == 2:
                for z in range(right, left - 1, -1):
                    ans.append(arr[down][z])
                down -= 1
            elif dir == 3:
                for w in range(down, top - 1, -1):
                    ans.append(arr[w][left])
                left += 1
            dir = (dir + 1) % 4
        return ans