class Solution:

    def encode(self, strs: list[str]) -> str:
        encodedString = ""
        for string in strs:
            countLetters = 0
            for letter in string:
                countLetters += 1
            encodedString = encodedString + f"{countLetters}#{string}"
        return encodedString
            
        

    def decode(self, s: str) -> list[str]:
        decodedArr = []

        i = 0
        while(i<len(s)):
            count=''
            while(s[i] != '#'):
                count = count+ s[i]
                i+=1
            
            countNum = int(count)
            word = ''
            j=0
            if(s[i] == '#'):
              i+=1
              while(j<countNum):
                  word += s[i]
                  j+=1
                  i+=1
            
            decodedArr.append(word)

        return decodedArr
            
