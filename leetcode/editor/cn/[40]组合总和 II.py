# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics 数组 回溯 👍 1233 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.used = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        self.used = [False] * n
        candidates.sort()
        self.dfs(0, 0, target, candidates)
        return self.ans

    def dfs(self, i, s, target, candidates):
        if s == target:
            self.ans.append(self.path.copy())
            return
        for j in range(i, len(candidates)):
            if s + candidates[j] > target:
                return
            if j > 0 and candidates[j] == candidates[j - 1] and self.used[j - 1] == False:
                continue
            s += candidates[j]
            self.path.append(candidates[j])
            self.used[j] = True
            self.dfs(j + 1, s, target, candidates)
            self.used[j] = False
            self.path.pop()
            s -= candidates[j]
# leetcode submit region end(Prohibit modification and deletion)
