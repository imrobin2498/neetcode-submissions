class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min_sum = nums[0]
        curr_max_sum = nums[0]
        min_sum = nums[0]
        max_sum = nums[0]
        total_sum = nums[0]

        for i in range(1, len(nums)):
            curr_min_sum = min(nums[i], curr_min_sum + nums[i])
            curr_max_sum = max(nums[i], curr_max_sum + nums[i])
            min_sum = min(min_sum, curr_min_sum)
            max_sum = max(max_sum, curr_max_sum)
            total_sum += nums[i]

        if max_sum < 0:
            return max_sum
        circular_sum = total_sum - min_sum
        return max(circular_sum, max_sum)
