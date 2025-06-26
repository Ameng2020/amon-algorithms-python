from typing import List


# ✅ Completed
def findLength(nums1:List[int], nums2: List[int]) -> int:
    m,n = len(nums1),len(nums2)
    dp = [0] * (n + 1)
    max_len = 0

    for i in range(1, m + 1):
        prev = 0  # 代表dp[i-1][j-1]
        for j in range(n, 0, -1):
            temp  = dp[j]
            if nums1[i - 1] == nums2[j - 1]:
                dp[j] = prev + 1
                max_len = max(max_len, dp[j])

            else:
                dp[j] = 0
            
            prev = temp

    return max_len



if __name__ == "__main__":
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    print(findLength(nums1,nums2))