class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        goodString = list(s)
        while(i < len(goodString)-1):
            print(goodString[i])
            print(ord(goodString[i]))
            if (ord(goodString[i])-ord(goodString[i+1])) == 32 or (ord(goodString[i])-ord(goodString[i+1])) == -32:
                goodString.pop(i)
                goodString.pop(i)
                i=0
            else:
                i+=1
                    
        return "".join(goodString)
