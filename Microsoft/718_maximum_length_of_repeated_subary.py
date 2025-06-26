"""
# 题目 最长重复子数组
给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。

 

示例 1：

输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。
示例 2：

输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5
 

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""


"""
目标是找到两个数组中 最长的公共子数组长度（子数组是连续的）

动态规划
定义一个二维数组dp[i][j]表示
nums1[0:i] 和 nums[0:j]的结尾处最长公共子数组的长度

使用二维 DP
"""

from typing import List

# ✅ Completed
def findLength(nums1:List[int], nums2:List[int]) -> int:
    m,n = len(nums1),len(nums2)
    # 初始化 dp 数组，默认值为0
    dp = [[0] * (n + 1) for _ in range(m+1)]
    max_len = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] == dp[i-1][j-1] + 1
                max_len = max(max_len,dp[i][j])


    return max_len


if __name__ == "__main__":
    print(findLength())