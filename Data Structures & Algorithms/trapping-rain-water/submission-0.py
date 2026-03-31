class Solution:
    def trap_array(self, height: List[int]) -> int:
        # water_i = min(left_max, right_max) - height_i
        n = len(height)
        if n == 0:
            return 0
        left_max = [0]*n
        right_max = [0]*n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n - 1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
        
# 这个个算法之所以高效，是因为它每一步都做了一个贪心的假设：
# 当你在左侧 l 且发现 left_max < right_max 时
# 你不需要知道 l 和 r 之间是否还有比 right_max 更高的柱子。

# 你只需要确定“右边有个大个子挡着”，那么左边的水位就绝对不会流向右边。
# 这种只看局部最值就决定当前步的操作就是贪心。
    def trap(self, height):
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0

        while l < r:
            # left is the bottleneck, w
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res




