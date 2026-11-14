class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1

        group = []
        for num in count:
            group.append([count[num], num])
        group.sort()

        result = []
        while(len(result) < k):
            last = group.pop()
            result.append(last[1])
        
        return result;