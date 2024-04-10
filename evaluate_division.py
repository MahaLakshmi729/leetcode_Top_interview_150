class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(g,source,target, v):
            if source not in g or source in v:return math.inf
            if source==target: return 1
            v.add(source)
            if source not in g or not g[source]: return math.inf
            for node in g[source]:
                d=dfs(g,node[0],target,v)
                if d !=math.inf:return node[1]*d
            return math.inf

        g={}
        ans=[]
        for i,eq in enumerate(equations): 
            if eq[0] not in g:g[eq[0]]=[]
            if eq[1] not in g:g[eq[1]]=[]
            g[eq[0]].append((eq[1],values[i]))
            g[eq[1]].append((eq[0],1.0/values[i]))
        
        for q in queries:
            d=dfs(g,q[0],q[1],set())
            if d==math.inf:ans.append(-1)
            else: ans.append(d)
        return ans
