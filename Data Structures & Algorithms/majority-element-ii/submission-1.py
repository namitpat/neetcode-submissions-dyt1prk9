class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element=[]
        visited=set()
        length=len(nums) // 3
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            count=0
            for j in range(i,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count>length:
                element.append(nums[i])
        return element

