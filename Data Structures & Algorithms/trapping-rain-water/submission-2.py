class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(height[l], l_max)
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                res += r_max - height[r]
        return res