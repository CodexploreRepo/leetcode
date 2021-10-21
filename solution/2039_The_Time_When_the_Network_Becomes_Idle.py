from collections import deque
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        """
        n servers: 0 to n-1
            master_server =  server 0
            data servers  = 1 to n-1
        edges: [[Ui, Vi]] message channel btw Ui and Vi, w = 1
        
        Since this is un-weighted graph,
        Distance from master_server to data server is the same as BFS-tree level traversal
        """
        n = len(patience)

        adj = {v: [] for v in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        level, dist, visited = 0, [0]*n, [False]*n
        queue = deque([0])
        visited[0] = True
        
        while(queue):
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                dist[curr] = level
                for v in adj[curr]:
                    if not visited[v]:
                        queue.append(v)
                        visited[v] = True
            level+=1
        travel_time = [2*d for d in dist]

        max_time = 0
        for i in range(1, n):
            #extra number of payload before the first message arrive back to data server.
            #since a data server can only send a message before first message arrives back."
            #and first message arrives at travel_time[i]*2. so "(travel_time[i]*2-1)"
            last_time = travel_time[i] - 1
            last_msg  = (last_time //patience[i])* patience[i]
            # maximum time = last message time + message travel time
            max_time = max(max_time, last_msg + travel_time[i])

        return max_time + 1
            
            
