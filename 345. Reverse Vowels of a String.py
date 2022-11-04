class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowls = ['a','e','i','o','u']
        letters = []
        index = []
        stringList = list(s)
        for charIndex in range(0,len(stringList)):
            char = stringList[charIndex]
            if char.lower() in vowls:
                letters.append(char)
                index.append(charIndex)
        for charIndex in range(0,len(letters)):
            stringList[index[len(letters) - charIndex - 1]] = letters[charIndex]

        return ''.join(stringList)
