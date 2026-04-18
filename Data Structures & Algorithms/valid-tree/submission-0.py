class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        adj = {i:[] for i in range(n)}
        for v ,e in edges:
            adj[v].append(e)
            adj[e].append(v)


        visit = set()

        def dfs(node , prev):
            if node in visit:
                return False

            visit.add(node)
            for new in adj[node]:
                if new == prev:
                    continue
                if not dfs(new , node):
                    return False

            return True

        return dfs(0,-1) and len(visit) == n




