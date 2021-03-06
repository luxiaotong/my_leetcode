#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (56.37%)
# Likes:    209
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 71.3K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数是不是“快乐数”。
# 
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
# 1。如果可以变为 1，那么这个数就是快乐数。
# 
# 示例: 
# 
# 输入: 19
# 输出: true
# 解释: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#

# @lc code=start
class Solution:
    def bitSquareSum(self, n: int) -> int:
        ans = 0
        while n > 0:
            y = n % 10
            ans += y ** 2
            n = n//10
        return ans
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
            if slow == fast:
                return slow == 1
        
# @lc code=end

