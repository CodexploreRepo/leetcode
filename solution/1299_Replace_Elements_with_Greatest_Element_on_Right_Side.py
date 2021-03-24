class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrLen = len(arr)
        if arrLen == 1:
            return [-1]
        
        curMax = -1
        for i in range(arrLen -1, -1,-1):
            temp = arr[i]
            arr[i] = curMax
            curMax = max(temp, curMax)
    
        return arr
