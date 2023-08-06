class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        i=0
        l=len(s)
        nums={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        while(i<l):
            digit=s[i]
            if(i==l-1):
                a=a+nums[digit]
                break
            nex=s[i+1]
            if(digit=='I'):
                if(nex=='V' or nex=='X'):
                    a=a+nums[nex]-nums[digit]
                    i=i+2
                    continue
                else:
                    a=a+nums[digit]
            elif(digit=='X'):
                 if(nex=='L' or nex=='C'):
                    a=a+nums[nex]-nums[digit]
                    i=i+2
                    continue
                 else:
                    a=a+nums[digit]
            elif(digit=='C'):
                 if(nex=='D' or nex=='M'):
                    a=a+nums[nex]-nums[digit]
                    i=i+2
                    continue
                 else:
                    a=a+nums[digit]
            else:
                a=a+nums[digit]
            i=i+1
        return a