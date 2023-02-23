class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        sum_wel=[]
        for i in accounts:
            sum_wel.append(sum(i))
        return max(sum_wel)  