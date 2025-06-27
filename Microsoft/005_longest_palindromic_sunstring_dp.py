
"""
最长回文字符串

动态规划解法
"""

def longestPalindrome(s:str) -> str:
  n = len(s)
  if n < 2:
      return s
  
  dp = [[False] * n for _ in range(n)]
  print("step1:",dp)
  start = 0
  max_len = 1

  # 所有长度为1的子串都是回文
  for i in range(n):
      dp[i][i] = True

  print("step2",dp)
  
  for i in range(n-1,-1,-1):
   print(f"i:{i}")
   for j in range(i+1,n):
      print(f"j:{j}")
      if s[i] == s[j]:
         if j - i == 1 or dp[i+1][j-1]:
            dp[i][j] = True
            if j - i + 1 > max_len:
               max_len = j - i + 1
               start = i

   print("="*10)

  return s[start:start + max_len]



if __name__ == "__main__":
   test_str = "babad"
   res = longestPalindrome(test_str)
   print(res)
  