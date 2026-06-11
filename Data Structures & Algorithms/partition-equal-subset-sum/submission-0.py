class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        dp = set([0])
        target = sum(nums) // 2

        for i in range(len(nums)):
            dp2 = dp.copy()
            for t in dp:
                if t+nums[i] == target:
                    return True
                dp2.add(t+nums[i])
            dp = dp2
        return False
                

