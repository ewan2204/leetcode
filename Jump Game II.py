class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps_to_end = [0]

        
        for i in range(len(nums) - 2, -1 , -1):
            min_jump_count = 9999
            for jump in range(i, i + nums[i]):
                if(jump >= len(nums)-1):
                    min_jump_count = min(1, min_jump_count)
                    break
                else:
                    min_jump_count = min(min_jump_count, 1 + min_jumps_to_end[len(nums) - (jump + 2)])
            min_jumps_to_end.append(min_jump_count)
        return min_jumps_to_end[-1]
