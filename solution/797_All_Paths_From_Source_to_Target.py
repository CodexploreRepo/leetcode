class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Nodes: 0 to n-1, where start = Node(0), target = Node(n-1)
        """
        n = len(graph)

        def DFS(u, path):
            if u == (n-1): res.append(path)
            else:
                for v in graph[u]:
                    DFS(v, path+[v])

        res = []
        DFS(0, [0])
        return res
            
