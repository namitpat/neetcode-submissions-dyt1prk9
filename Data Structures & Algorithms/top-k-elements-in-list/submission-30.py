class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}     
        final=[0]*k
        for i in range(len(nums)):     
            if  nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]] = 1

        sorted_list = sorted(hashmap.items(), key=lambda x: x[1],reverse=True)
        limit = min(k, len(sorted_list))
        for i in range(limit):
            final[i]=(sorted_list[i][0])
        
        return final

    
                    
                
            

        