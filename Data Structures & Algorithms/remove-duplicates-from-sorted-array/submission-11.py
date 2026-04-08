class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=len(nums)-1
        j=i-1
        while i!=0:
            if nums[i]==nums[j]:
                nums.pop(j)
                i-=1
                j-=1
                continue
            
            i-=1
            j-=1

            

        k=len(nums)
        return k




        

        