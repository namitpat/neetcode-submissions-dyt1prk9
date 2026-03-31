class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[j]<nums[i]:
        #             temp=nums[i]
        #             nums[i]=nums[j]
        #             nums[j]=temp
        index=0
        value=0
        counts=[0]*3
        for num in  nums:
            counts[num]+=1

        for count in  counts:
            for i in range(count,0,-1):
                nums[index]=value
                index+=1
            value+=1





        