class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        
        word=strs[0]#bat
        for i in range(len(word)):
            k=0
            letter=word[i]#b a
            for j in range(1,len(strs)):
                word2=strs[j]#bag
                if i>=len(word2):
                    return s
                letter2=word2[i]#b
                if letter==letter2:
                    k=k+1
                    continue
                else:
                    return s
            if k==(len(strs))-1:
                s=s+letter
        return s
            
                


                
                
                


        
        