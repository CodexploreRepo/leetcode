class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_vol = 0, len(height)-1, 0
        while(left < right):
            if height[left] > height[right]:
                vol = height[right]*(right - left)
                right-= 1
            else:
                vol = height[left]*(right - left)
                left += 1
            max_vol = max(max_vol, vol)
        return max_vol
