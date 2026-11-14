class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeatedNums = {}
        for num in nums:
            if num in repeatedNums.keys():
                repeatedNums[num] += 1
            else:
                repeatedNums[num] = 1
        
        keys = list(repeatedNums.keys())
        vals = list(repeatedNums.values())
        result = []
        for i in range(k):
            maxVal = max(vals)
            maxValIndex = vals.index(maxVal)
            vals.pop(maxValIndex)
            result.append(keys[maxValIndex])
            keys.pop(maxValIndex)
        
        return result
