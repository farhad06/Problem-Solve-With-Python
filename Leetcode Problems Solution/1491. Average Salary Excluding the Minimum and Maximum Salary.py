class Solution:
    def average(self, salary: List[int]) -> float:
        # mini=min(salary)
        # maxi=max(salary)
        s=0
        for i in range(len(salary)):
            s=s+salary[i]
            if salary[i]==max(salary):
                maxi=salary[i]
            if salary[i]==min(salary):
                mini=salary[i] 
        s=s-maxi-mini
        avg=(s/(len(salary)-2))
        return avg      
