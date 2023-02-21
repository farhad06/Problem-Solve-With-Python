class Solution:
    def finalValueAfterOperations(self, operation: List[str]) -> int:
        x=0
        for operator in operation:
            if "+" in operator:
                x+=1
            if "-" in operator:
                x-=1
        return x            
