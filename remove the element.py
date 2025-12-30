class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #declaring two pointers, one at starting another at ending
        left = 0
        right = len(nums) - 1
        #Initializing loop 
        while left <= right:
            #comparing value of left with the val value
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return right + 1