class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        backwords = 0
        dictionary = dict()
        for word in words:
            reverseWord = word[::-1]
            a = dictionary.get(reverseWord)
            if a and a != 0:
                dictionary[reverseWord] = a - 1
                backwords += 4
            else:
                b = dictionary.get(word)
                if(b):
                    dictionary[word] = 1 + b
                else:
                    dictionary[word] = 1
        for key, value in dictionary.items(): 
            if value:
                if key == key[::-1]:
                    return backwords + 2
        return backwords
