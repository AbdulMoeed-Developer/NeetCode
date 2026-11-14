class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key in anagrams.keys():
                anagrams[key].append(strs[i])
            else:
                anagrams[key] = [strs[i]]

        return list(anagrams.values())