from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        #We will use Set, instead of List to check if an item is contained within it "x in s"
        deadends, visited = set(deadends), set(start)
         
        if start in deadends: return -1 ##if start in deadends, then stop
        if start == target: return 0 #if start == target => return 0
        
        turn = 0 
        queue = deque([start]) # Initializing a queue
        
        while(queue):
            turn+= 1
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == target: return turn - 1 
                if curr not in deadends and curr not in visited:
                    #to ensure curr not in deadends and not in visited
                    visited.add(curr)
                    for neighbor in self.neighbors(curr):
                        queue.append(neighbor)
        return -1
                    
    
    def neighbors(self, s):
        """
        Output: To return possible combinations of s, for ex: "0000", for each move
        """
        res = []
        n = len(s)
        for i in range(0,n):
            #print(s[:i] + " " + s[i] + " " +s[i+1:])
            res.append(s[:i] + str((int(s[i])+1)%10) + s[i+1:]) #Either moving up 
            res.append(s[:i] + str((int(s[i])-1)%10) + s[i+1:]) #Either moving down
        return res
