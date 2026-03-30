# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         final=[]
#         for i in range(len(strs)):
#             result=[]
#             word=strs[i]
#             result.append(word)
#             for j in range(i+1,len(strs)):
#                 countS,countT={}, {}
#                 word2=strs[j]
#                 if len(word) != len(word2):
#                     continue
#                 for k in range(len(word)):
#                     countS[word[i]]=1+countS.get(word[i],0)
#                     countT[word2[i]]=1+countT.get(word2[i],0)
#                 for c in countS:
#                     if countS[c] != countT.get(c,0):
#                         continue
#                 result.append(word2)
#                 strs.pop(j)
#             final.append([result])
#         return final


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        visited = set()

        for i in range(len(strs)):
            if i in visited:
                continue

            result = []
            word = strs[i]
            result.append(word)
            visited.add(i)

            for j in range(i + 1, len(strs)):
                if j in visited:
                    continue

                word2 = strs[j]

                if len(word) != len(word2):
                    continue

                countS, countT = {}, {}

                for k in range(len(word)):   # FIXED variable
                    countS[word[k]] = 1 + countS.get(word[k], 0)
                    countT[word2[k]] = 1 + countT.get(word2[k], 0)

                # Proper check
                is_anagram = True
                for c in countS:
                    if countS[c] != countT.get(c, 0):
                        is_anagram = False
                        break

                if is_anagram:
                    result.append(word2)
                    visited.add(j)

            final.append(result)   # FIXED nesting

        return final

            
                
                
            


        
       

        
        
      