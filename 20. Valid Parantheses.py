class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d1={'{':'}','(':')','[':']'}
        if len(s)%2==1:
            return False
        for c in s:
            if c in d1:
                stack.append(c)
            elif c==')' and stack:
                if stack.pop()!='(':
                    return False
            elif c=='}' and stack:
                if stack.pop()!='{':
                    return False
            elif c==']' and stack:
                if stack.pop()!='[':
                    return False
            else:
                return False
        return True if len(stack)==0 else False
