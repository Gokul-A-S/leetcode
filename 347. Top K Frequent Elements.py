 def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap=defaultdict(int)
        for el in nums:
            countMap[el]+=1
        res=sorted(countMap.items(),key=lambda x:x[1],reverse=True)
        ret=[]
        for item in res:
            ret.append(item[0])
        print(ret[:k])
        