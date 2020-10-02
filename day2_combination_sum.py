class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target+1)]
        
        for c in candidates:
            for t in range(1,target+1):
                if t<c:
                    continue
                if t == c:
                    dp[t].append([c])
                else:
                    for plist in dp[t-c]:
                        dp[t].append(plist+[c])
        return dp[target]
        