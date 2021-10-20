class Solution:
    """
    Kruskal Algorithm
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        if size == 0: return 0
        
        pq = [] #create a heap to keep track on the smallest weigthed edges
        uf = UnionFind(size) #create a UnionFind Data Structure to store the vertices in MST

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                # Calculate the distance between two coordinates.
                cost = abs(x1 - x2) + abs(y1 - y2)
                #Create an Edge Object to store Vertex i & j and store their corresponding Cost
                edge = Edge(i, j, cost)
                pq.append(edge) #Put the Edge into the priority queue
        
        # Convert pq into a heap.
        heapq.heapify(pq)

        
        result = 0
        count = size - 1 #N - 1
        #Kruskal Algorithm
        while pq and count > 0:
            edge = heapq.heappop(pq) #Pop the Min Weighted Edge
            if not uf.connected(edge.point1, edge.point2): #If point1 and poin2 is NOT connect in uf
                uf.union(edge.point1, edge.point2) #Connect them together
                result += edge.cost #result is added by that Weighted Edge
                count -= 1
        return result

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class UnionFind:
    #Union and Find Rank
    def __init__(self, size):
        self.root = [i for i in range(size)] #to init the root of each node = itself
        self.rank = [1] * size #to init the rank of all node = 1

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]: #if Rank X > Rank Y, X will be parent of Y
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]: #if Rank X < Rank Y, Y will be parent of X
                self.root[rootX] = rootY
            else: #if Rank X = Rank Y, X will be parent of Y, increase rank of X by 1
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    """
    Prim Algorithm
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        if size == 0: return 0
        
        pq = [] #create a heap to keep track on the smallest weigthed edges
        visited = [False]*size #Create a visited array as False initally
        
        x1, y1 = points[0] #Start randomly at point 0
        for j in range(1, size):
            x2, y2 = points[j]
            # Calculate the distance between two coordinates.
            cost = abs(x1 - x2) + abs(y1 - y2)
            #Create an Edge Object to store Vertex 0 & j and store their corresponding Cost
            edge = Edge(0, j, cost)
            pq.append(edge) #Put all Edges connect to Point 0 into the priority queue
        
        # Convert pq into a heap.
        heapq.heapify(pq)
        
        visited[0] = True #Mark Point 0 as visited
        result = 0 #Init Result
        count = size - 1 #N - 1
        #Prim's Algorithm
        while pq and count > 0:
            edge = heapq.heappop(pq) #Pop the Min Weighted Edges
            point1 = edge.point1 #Point 0 
            point2 = edge.point2 #The other point connected to Point 0, called as Point 2
            cost = edge.cost
            
            if not visited[point2]: #If Point2 is not visited
                result += edge.cost #result is added by that Weighted Edge
                visited[point2] = True #Marked Pointed 2 as visited
                for j in range(size): #Compute all the edges of Point2 to un-visited Vertex 
                    if not visited[j]:
                        x1, y1 = points[point2]
                        x2, y2 = points[j]
                        cost = abs(x1 - x2) + abs(y1 - y2)
                        edge = Edge(point2, j, cost)
                        heapq.heappush(pq,edge) #Put the Edge into the priority queue
                count -= 1
        return result

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

