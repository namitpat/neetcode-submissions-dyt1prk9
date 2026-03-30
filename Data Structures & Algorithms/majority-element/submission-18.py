# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         visited=set()
#         target=0
#         k=1
#         n=len(nums)
#         n=n/2
#         for i in range(len(nums)):
#             k=1
#             if nums[i] in visited:
#                 continue
#             visited.add(nums[i])
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     k=k+1
#             if k>n:
#                 target=nums[i]
#         return target
               
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target=0
        k=1
        n=len(nums)
        n=n/2
        for i in range(len(nums)):
            k=1
            if target !=nums[i]:
                for j in range(i+1,len(nums)):
                    if nums[i]==nums[j]:
                        k=k+1
                if k>n:
                    target=nums[i]

            
        return target         


            
            
            


                    

        
        