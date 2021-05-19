'''
227. 基本计算器 II
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
示例 1：
输入：s = "3+2*2"
输出：7
示例 2：
输入：s = " 3/2 "
输出：1
示例 3：
输入：s = " 3+5 / 2 "
输出：5
提示：
1 <= s.length <= 3 * 105
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
题目数据保证答案是一个 32-bit 整数
'''
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        preSign='+'
        stack =[]
        n = len(s)
        for i in range(n):
            if s[i] !=' ' and s[i].isnumeric():
                num = num*10 + ord(s[i])-ord('0')
            if i == n-1 or s[i] in '+-*/':
                if preSign =='+':
                    stack.append(num)
                elif preSign =='-':
                    stack.append(-num)
                elif preSign =='*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                preSign = s[i]
                num = 0
        return sum(stack)

if __name__ =='__main__':
    ss = Solution()
    s = "3+2*2"
    print('1',ss.calculate(s))
    s = " 3/2 "
    print('1',ss.calculate(s))
    s = " 3+5 / 2 "
    print('1',ss.calculate(s))
    s = "14-3/2"
    print('1',ss.calculate(s))
