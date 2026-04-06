class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=0
        hashset=set()
        for num in nums:
            if num in hashset:
                continue
            hashset.add(num) 

        for i in range(1,len(hashset)+1):
            if i==len(hashset) and i in hashset:
                return i+1
            if i in hashset:
                continue
            if i not in hashset:
                return i
            
                   
        

            
            