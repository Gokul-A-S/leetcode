class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        strn=[]
        op=[]
        for row in mat:
            try:
                strn.append(row.index(0))
            except:
                strn.append(len(row))
        print(strn)
        for j in range(k):
            el=min(strn)
            i=strn.index(el)
            op.append(i)
            strn[i]=''
        return op