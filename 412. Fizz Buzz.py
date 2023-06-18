 class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[None]*(n+1)
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):
                answer[i]='FizzBuzz'
            elif(i%3==0):
                answer[i]='Fizz'
            elif(i%5==0):
                answer[i]='Buzz'
            else:
                answer[i]="%s" %i
        return answer[1:n+1]