class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        for row in accounts:
            if(s<sum(row)):
                s=sum(row)
        return s