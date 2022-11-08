class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        listChar = list(s)

        if(k == 1):
            min = s
            for i in range(1,len(listChar)):
                min = min if min < "".join(listChar[i:]+listChar[:i]) else "".join(listChar[i:]+listChar[:i])
            return min
        else:
            listChar.sort()
            return "".join(listChar)
