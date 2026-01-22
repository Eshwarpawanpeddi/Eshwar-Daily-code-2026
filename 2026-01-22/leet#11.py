class Solution:
    def area(i,j):
        return i*j

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = 0
        max_area = 0
        for i in range(len(height)):
            for j in range(len(height)):
                temp_area = area(height[i], height[j])
                if temp_area > max_area:
                    max_area = temp_area
        return max_area