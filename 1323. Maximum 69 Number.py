class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        #Change the first 6 to a 9
        char = str(num)
        print("aaa")
        for i in range(len(char)-1 ,-1, -1):
            a = (num / (10 ** i)) % 10
            if(a == 6):
                return num + 3 * 10 ** i
        return num
