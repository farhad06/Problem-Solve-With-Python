class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if (nums[i]+diff in nums) and (nums[i]+2*diff in nums):
                count+=1
        return count        