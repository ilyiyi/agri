# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。 
# 
#  例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：6 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n < 2^31 
#  
# 
#  注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/ 
# 
#  Related Topics 递归 数学 动态规划 👍 400 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        high = n // 10
        cur = n % 10
        low = 0
        # 表示当前位数，初始为个位
        d = 1
        ans = 0
        while high or cur:
            if cur == 0:
                ans += high * d
            elif cur == 1:
                ans += high * d + low + 1
            else:
                ans += (high + 1) * d
            low += cur * d
            cur = high % 10
            high //= 10
            d *= 10
        return ans
# leetcode submit region end(Prohibit modification and deletion)
