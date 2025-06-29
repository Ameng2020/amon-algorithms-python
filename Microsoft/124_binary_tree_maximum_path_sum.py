"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

 

示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 

提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
"""
from typing import Optional


# ✅ Completed
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right



class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    self.max_sum = float('-inf')  # 全局最大路径


    def max_gain(node:Optional[TreeNode]) -> int:
        if not node:
          return 0
        
        # 计算左右子树最大贡献，如果为负值则视为0 （不选）
        left_gain= max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # 当前节点作为最高点时路径和
        current_max = node.val + left_gain + right_gain

        # 更新全局最大路径和
        self.max_sum = max(self.max_sum, current_max)

        # 返回当前节点最大可延续的路径
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)

    return self.max_sum