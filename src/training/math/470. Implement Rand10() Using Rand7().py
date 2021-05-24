'''
470. 用 Rand7() 实现 Rand10()
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。
示例 1:
输入: 1
输出: [7]
示例 2:
输入: 2
输出: [8,4]
示例 3:
输入: 3
输出: [8,1,10]
提示:
rand7 已定义。
传入参数: n 表示 rand10 的调用次数。
进阶:
rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?
'''
import random
def rand7():
    '''https://docs.python.org/3/library/random.html#random.randrange'''
    # print(random.random())
    # print(random.randint(0, 7))
    # print(random.randrange(10))
    # print(random.choice([1, 5, 6, 232, ]))
    return random.randrange(7)
class Solution:
    def rand10_1(self):
        """
        :rtype: int
        """
        row=col=0
        idx=41
        while idx >40:
            row, col = rand7(), rand7()
            idx= col+(row-1)*7 #二维变一维
        return 1+(idx-1)%10
    def rand10_2(self):
        """
        :rtype: int
        """
        pass
if __name__ =='__main__':
    s = Solution()
    print('1', s.rand10_1())
    print('1', s.rand10_2())

