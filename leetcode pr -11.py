class Solution:
    def maxArea(self, height: List[int]) -> int:
        #here we assign the positions of the pointers 
        left = 0
        right = len(height) - 1
        max_area = 0
        #looping of the 
        while left < right:
            h = min(height[left],height[right])
            w = right - left
            area = h * w
            max_area = max(area,max_area)
        #moving the pointers based on the conditions
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area

