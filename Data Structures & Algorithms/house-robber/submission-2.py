class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0]*len(nums)
        if (len(nums))<=2:
            return max(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[1], memo[0])

        for i in range(2, len(nums)):
            memo[i]= max(memo[i-1], nums[i]+memo[i-2])

        return memo[-1]
        