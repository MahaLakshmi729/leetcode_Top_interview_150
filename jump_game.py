class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #original destination is last index
        goal = len(nums)-1

        #check backwards
        for i in range(len(nums)-2,-1,-1):
            #if we can jump then update
            if i+nums[i] >= goal:
                goal = i

        #check if we can reach from first index
        return True if goal == 0 else False #return goal == 0