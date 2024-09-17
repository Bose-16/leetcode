class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1=s1.split()
        words2=s2.split()
        tot=words1+words2
        b=len(tot)
        count={}
        for i in tot:
            if i in count:
                 count[i] += 1
            else:
                  count[i] = 1
        distinct =[]
        for i in tot:
              if count[i]==1:
                    distinct.append(i)           
        print(distinct)
s1="this an apple is sweet"
s2="this an apple is sour"
print(Solution.uncommonFromSentences)
