class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexList = []
        for i in range(len(nums)):
            findNum = target - nums[i]
            
            for j in range(len(nums)):
                if nums[j] == findNum and j != i:
                    indexList.append(j)
                    indexList.append(i)
                    indexList.sort()
                    return(indexList)