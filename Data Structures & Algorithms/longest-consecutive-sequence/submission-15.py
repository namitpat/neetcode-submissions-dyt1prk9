class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=1
        current=1
        nums=sorted(nums)
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                current+=1
            else:
                longest=max(current,longest)
                current=1
            
        return max(longest, current)






        #     if i+1<len(nums):
        #         count.append(nums[i+1]-nums[i])
        
        # for i in range(len(count)):
        #     if count[i]==1 and i+1<len(count) and count[i+1]==1:
        #         final+=1
        #     if i+1<len(count) and count[i]==count[i+1]==0:
        #         continue
        #     else:
        #         main.append(final)
        #         final=0
        # main=sorted(main)
        # final=main[-1]
        # return final







        