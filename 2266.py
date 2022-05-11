"""
https://leetcode.cn/problems/count-number-of-texts/

author: labuladuo
date: 2022/5/11
"""


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7
        dp = [1 for _ in range(len(pressedKeys))]
        for i in range(1, len(pressedKeys)):
            dp[i] = dp[i - 1]
            if pressedKeys[i] == pressedKeys[i - 1]:
                dp[i] += 1 if i < 2 else dp[i - 2]
                if i >= 2 and pressedKeys[i] == pressedKeys[i - 2]:
                    dp[i] += 1 if i < 3 else dp[i - 3]
                    if i >= 3 and (pressedKeys[i] == '7' or pressedKeys[i] == '9') and pressedKeys[i] == pressedKeys[i - 3]:
                        dp[i] += 1 if i < 4 else dp[i - 4]
        return dp[len(pressedKeys) - 1] % mod


if __name__ == '__main__':
    s = Solution()
    res = s.countTexts("222222222222222222222222222222222222")
    print(res)
