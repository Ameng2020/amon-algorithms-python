# ✅ Completed
from typing import List

"""
题目：
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
"""

def twoSum(nums:List[int],target:int) -> List[int]:

  seen = {}

  for i,num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [seen[complement],i]
    
    seen[num] = i

  
  return []