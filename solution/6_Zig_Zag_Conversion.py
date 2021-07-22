class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        numRows = 4
        Row 0: 0 6 12      => 0 + 6 + 6
        Row 1: 1 5 7 11 13 => 1 + 4 + 2 + 4 + 2
        Row 2: 2 4 8 10    => 2 + 2 + 4 + 2
        Row 3: 3 9         => 3 + 6
        
        cycle = 2*numRows - 2 (from numRows = 3 and 4)
        
        Re-write: row j, which is not first and last row
        Row 1: 1 5 7 11 13 => 1 + (6-2) + 6 + (6-2) + 
        Row j:             => j + (cycle-2i) + cycle + (cycle-2i) + cycle
        
        Time: O(n) as looping through only the whole string 
        Space: O(n)
        """
        #Special Case
        if numRows == 1: 
            return s
        res=[]
        cycle = 2*numRows - 2
        #Looping through First numRows(th) character
        for i in range(0, numRows):
            #Going through Each Row j:
            for j in range(i, len(s), cycle):
                res.append(s[j])
                #If j is not first and last row, need to include mid-element (k)
                k = j + cycle - 2*i
                if (i !=0) and (i != numRows -1)  and (k < len(s)):
                    res.append(s[k])
        return "".join(res)
                
            
