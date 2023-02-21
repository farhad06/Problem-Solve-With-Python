class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        arr_sum=0
        digit_sum=0
        for num in nums:
            arr_sum+=num
            while num>0:
                digit_sum+=num%10
            #     digit_sum+=r
                num//=10 
        return abs(arr_sum-digit_sum)        
