class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for s in ransomNote:
            canConstruct=True
            if(s in magazine):
                magazine=magazine.replace(s,'',1)
            else:
                canConstruct=False
                break
        return canConstruct