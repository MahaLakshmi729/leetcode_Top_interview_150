class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points) 
        maxP = 0 
        for i in range(n):
            X = points[i][0]
            Y = points[i][1]
            map = {} 
            for j in range(i+1, n):
                dx = points[j][0] - X
                dy = points[j][1] - Y 
                if(dx != 0): 
                    d = dy/dx
                    if d in map:
                        map[d] = map[d] + 1
                    else:
                        map[d] = 1 
                else:
                    if 20001.0 in map:
                        map[20001.0] = map[20001.0] + 1
                    else:
                        map[20001.0] = 1 
            if map:
                maxP = max(maxP, max(map.values())) 
        return maxP + 1