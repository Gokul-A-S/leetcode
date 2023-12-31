class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hashMap=defaultdict(int)
        for char in s:
            hashMap[char]+=1
        for char in t:
            if(hashMap[char]==0):
                return False
            hashMap[char]-=1
        return True