class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            main=nums[i]
            mul=1
            for j in range (len(nums)):
                if i==j:
                    continue
                mul=mul*nums[j]
            output.append(mul)
        return output
                
        