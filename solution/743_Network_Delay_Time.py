class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Creat a list of vertex
        vertex = [v for v in range(1,n+1)] 
        #Create a adj list contain the (adj vertex + its weight)
        adj = {u: {} for u in vertex}
        for u, v, w in times:
            adj[u][v] = w
        #Initialize the distance, k= source, so {k:0} means distance from k to k = 0 
        dist = {k:0}
        heap = []
        #Initialize the heap to keep track all the min_dist from source k to all other vertices
        for v in vertex:
            if v!= k:
                #if v in adj[u], then (weight, v) added to heap, otherwise add (inf, v)
                heapq.heappush(heap, [adj[k][v] if v in adj[k] else math.inf, v])
        
        #Loop through the heap
        while len(heap) > 0:
            #Popout the min_weight from the heap
            min_dist, v = heapq.heappop(heap) #min_dist and vertex v
            dist[v] = min_dist #dist from source to v = min_dist
            for i in range(len(heap)):
                if heap[i][1] in adj[v]: #check v's neighbors
                    #if the distane from source to a v's neighbor > distance from source to v + dist from v to the v's neighbor 
                    #then update the distane from source to a v's neighbor to the heap 
                    heap[i][0] = min(heap[i][0], min_dist + adj[v][heap[i][1] ])
            #heapify the heap after updated
            heapq.heapify(heap)
        max_time = max(dist.values())
        return max_time if max_time != math.inf else -1
