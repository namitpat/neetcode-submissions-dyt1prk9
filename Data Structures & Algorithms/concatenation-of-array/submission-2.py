class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        j=n*2
        ans=[0]*j
        
        for i in range(len(nums)):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return ans
            
        