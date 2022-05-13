"""
https://leetcode.cn/problems/string-to-integer-atoi/

author: labuladuo
date: 2022/4/14
"""
import re


class Solution:
    def myFunction(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.lstrip()
        num_re = re.compile(r'^[\+\-]?\d+')
        num = num_re.findall(str)
        num = int(*num)
        return max(min(num, INT_MAX), INT_MIN)


if __name__ == '__main__':
    s = Solution()
    print(s.myFunction("0123"))
