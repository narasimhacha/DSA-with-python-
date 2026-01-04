class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxSum = currentSum

    # Slide window
        for i in range(k, len(nums)):
            currentSum = currentSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, currentSum)

        return maxSum / k
        