# Problem: Trapping Rainwater
# Author: Trl Rizu
# Solution from: Neetcode
# Taken from: https://leetcode.com/problems/trapping-rain-water/

# You are given an array of non-negative integers height which represent an elevation map. 
# Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example
# Input: height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9


#Stack
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res

#Two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res