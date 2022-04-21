"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

author: labuladuo
date: 2022/4/13
"""


def myFunction(s):
    i = 0
    j = 0
    length = len(s)
    if length == 0:
        return 0
    maxLen = 0
    res = ""
    while j < length:
        while s[j] in res:
            res = res[1:]
        res += s[i]
        i = i + 1
        j = j + 1
        maxLen = len(res) if maxLen < len(res) else maxLen
    return maxLen


if __name__ == '__main__':
    ss = "abcabcbb"
    print(myFunction(ss))
