'''
567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

 

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

提示：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass
if __name__ =='__main__':
    s = Solution()
    s1 = "ab" 
    s2 = "eidbaooo"
    print('1',s.checkInclusion(s1,s2))
    s1= "ab" 
    s2 = "eidboaoo"
    print('1',s.checkInclusion(s1,s2))