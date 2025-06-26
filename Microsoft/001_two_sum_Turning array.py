# ✅ Completed
from typing import List

"""
换一个数据结构，看面试者是否能够利用规则，在时间复杂度上进一步优化。

当然有序数组也可以改成二叉树等其他数据结构，或者是一些具备某特性的数据结构。有序数组的话，注意用二分查找，可以把时间复杂度降到 O （ logn ），注意哈希表的构建时间复杂度是 O （ n ），能直接用二分查找就直接用，不要考虑哈希。

真题：

给定一个“拐弯数组”，由两个有序数组拼接而成，但两数组升降序相反。 如：[1,2,3] + [6, 5, 4] ---> [1,2,3, 6, 5,4]。 要求在拐弯数组中找到给定的 target 。

这题如果用哈希，虽然是 O(n)，但不是最优，没有用到数组的特性。我们先用二分法找到拐点，再到两个有序数组中二分，把复杂度优化到 O （ logn ）


描述：

给定一个“拐弯数组” arr，它由两个单调有序数组拼接而成：

第一部分是升序排列

第二部分是降序排列

两部分长度均 ≥ 1

你的任务是在该数组中查找目标值 target，如果存在返回 True，否则返回 False。

你必须在 O(log n) 时间内完成该查找任务。
"""


def find_in_bending_array(arr: List[int],target: int) -> bool:

  def find_peak() -> int:
    # 找到峰值元素索引（拐点）
    left, right = 0, len(arr) - 1
    while left < right:
      mid = (left + right) // 2
      if arr[mid] < arr[mid + 1]:
        left = mid + 1
      else:
        right = mid

    return left
  

  def binary_search_asc(left:int, right: int) -> bool:
    while left <= right:
      mid = (left + right) // 2
      if arr[mid] == target:
        return True
      elif arr[mid] < target:
        left = mid + 1
      else:
        right = mid - 1

    return False
  

  def binary_search_desc(left: int, right:int ) -> bool:
    while left <= right:
      mid = (left + right) // 2
      if arr[mid] == target:
        return True
      elif arr[mid] > target:
        left = mid + 1
      else:
        right = mid + 1 

    return False

  peak = find_peak()

  return binary_search_asc(0,peak) or binary_search_desc(peak+1, len(arr) - 1)

