class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        nums2=[]
        for i in range(len(nums)):
            if val!=nums[i]:
                nums[k]=nums[i]
                k=k+1
        return k



        