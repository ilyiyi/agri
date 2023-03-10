# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。 
# 
#  字母和数字都属于字母数字字符。 
# 
#  给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "race a car"
# 输出：false
# 解释："raceacar" 不是回文串。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = " "
# 输出：true
# 解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
# 由于空字符串正着反着读都一样，所以是回文串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  s 仅由可打印的 ASCII 字符组成 
#  
# 
#  Related Topics 双指针 字符串 👍 610 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 判断是否为字母
        def check(t: str) -> bool:
            if 'a' <= t <= 'z' or 'A' <= t <= 'Z' or '0' <= t <= '9':
                return True
            return False

        def value(t: str) -> str:
            if 'A' <= t <= 'Z':
                return str.lower(t)
            else:
                return str.lower(t)

        i, j = 0, len(s) - 1
        while i < j:
            x = s[i]
            y = s[j]
            if not check(x):
                i += 1
            if not check(y):
                j -= 1
            if check(x) and check(y):
                if value(x) != value(y):
                    return False
                else:
                    i += 1
                    j -= 1
        return True


Solution().isPalindrome("A man, a plan, a canal: Panama")
# leetcode submit region end(Prohibit modification and deletion)
