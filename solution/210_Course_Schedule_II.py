class Solution:
    def __init__(self):
        self.color = None
        self.torder = None
        self.found_cycle = False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1 and prerequisites == []: return [0]
        #Step 1: Creating a adjlist graph = adj_course 
        adj_course = {u: [] for u in range(numCourses)}
        
        n = len(prerequisites)
        for i in range(n):
            adj_course[prerequisites[i][1]].append(prerequisites[i][0])
        #Step 2: Initialize the color flag & t_order list 
        self.color = {u: "WHITE" for u in adj_course}
        self.torder = []
        
        #Step 3: Apply DFS for any node which is not visited
        for u in adj_course:
            if self.color[u] == "WHITE":
                self.DFS_tsort(u,adj_course)
        #If flag found_cycle = True, return [] else: reversese the toder
        return [] if self.found_cycle else self.torder[::-1]
    
        
    def DFS_tsort(self, u, adj_course):
        self.color[u] = "GRAY"
        for v in adj_course[u]:
            if self.color[v] == "GRAY":
                #If color[v] == "GRAY", means that there is a cycle
                self.found_cycle = True
                return
            if self.color[v] == "WHITE":
                self.color[v] = "GRAY"
                self.DFS_tsort(v, adj_course)
        #Append the node into toder list
        self.torder.append(u)
        self.color[u] = "BLACK"
        
                
