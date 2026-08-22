class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newDict = {}
        newDict2 = {}
        for letter in s:
            if letter in newDict:
                newDict[letter] += 1
            else:
                newDict[letter] = 1
        
        for letter in t:
            if letter in newDict2:
                newDict2[letter] += 1
            else:
                newDict2[letter] = 1
        
        if(newDict == newDict2):
            return(True)
        else:
            return(False)
