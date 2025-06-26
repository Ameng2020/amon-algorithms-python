"""
# 最长回文字符串

给你一个字符串 s，找到 s 中最长的 回文 子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""
# ✅ Completed

def longestPalindrome(s:str) -> str:
  if not s:
      return ""
  
  start, end = 0,0

  def expandAroundCenter(left:int, right: int) -> tuple[int, int]:
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1

    return left + 1, right -1
  
  for i in range(len(s)):
     # 奇数中心
     l1, r1 = expandAroundCenter(i, i)

     # 偶数中心
     l2, r2 = expandAroundCenter(i, i+ 1)

     if r1-l1 > end - start:  
        start, end =l1,r1

     if r2-l2 > end -start:
        start, end = l2, r2

  return s[start:end+1]