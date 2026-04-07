class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=""
        n=min(len(word1),len(word2))
        for i in range(n):
            merge+=word1[i]+word2[i]
        
        if len(word1)>n:
            for i in range(n,len(word1)):
                merge+=word1[i]
        if len(word2)>n:
            for i in range(n,len(word2)):
                merge+=word2[i]

        return merge



        