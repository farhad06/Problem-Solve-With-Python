class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # arr=[]
        n=len(nums)
        for i in nums:
            if nums.count(i)==1:
                return i
        # return arr[0]    