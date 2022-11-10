class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in list(s):
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
