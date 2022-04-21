"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

author: labuladuo
date: 2022/4/12
"""


def myFunction(numList, targetNum):
    i = 0
    j = len(numList) - 1
    d = {}
    for index in range(len(numList)):
        if d.get(numList[index]) is not None:
            d.update({numList[index]: [d.get(numList[index]), index]})
        else:
            d.update({numList[index]: index})
    numList.sort()
    for n in range(len(numList)):
        if i > j:
            break
        if numList[i] + numList[j] == targetNum:
            if numList[i] == numList[j]:
                return d.get(numList[i])
            else:
                return [d.get(numList[i]), d.get(numList[j])]
        if numList[i] + numList[j] > targetNum:
            j = j - 1
        if numList[i] + numList[j] < targetNum:
            i = i + 1
    pass


def twoSum(numList, targetNum):
    hashmap = {}
    for i, num in enumerate(numList):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(targetNum - num)]
        # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
        hashmap[num] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(myFunction(nums, target))
