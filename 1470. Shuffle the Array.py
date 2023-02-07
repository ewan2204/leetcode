class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        outlist = []
        for i in range(0,n):
            outlist.append(nums[i])
            outlist.append(nums[i + n])

        return outlist
