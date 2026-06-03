class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0]*(len(cost)+1)
        for i in range(len(memo)):
            if i <= 1:
                memo[i] = cost[i]
            elif i < len(cost) :
                memo[i] = cost[i] + min(memo[i-1], memo[i-2])
            else:
                memo[i] = min(memo[i-1],memo[i-2])
        return memo[-1]
            