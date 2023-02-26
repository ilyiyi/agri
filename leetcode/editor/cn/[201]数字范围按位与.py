# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）
# 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：left = 5, right = 7
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：left = 0, right = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：left = 1, right = 2147483647
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= left <= right <= 2³¹ - 1 
#  
# 
#  Related Topics 位运算 👍 436 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right

# leetcode submit region end(Prohibit modification and deletion)
print(1 & 2 & 3)
print(5 & 6 & 7 & 8)
print(9 & 10 & 11 & 12 & 13)

print(7 & 8 & 9)
print(2 & 3)
print(8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16)
print(6 & 7)
