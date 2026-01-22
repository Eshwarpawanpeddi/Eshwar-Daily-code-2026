class Solution:
    def area(self,leng,i,j):
        if i<j:
            count = i
        else:            
            count = j
        return count * leng

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = 0
        max_area = 0
        leng = 0

        for i in range(len(height)):
            for j in range(len(height)):
                leng = j - i
                temp_area = self.area(leng,height[i], height[j])
                if temp_area > max_area:
                    max_area = temp_area
        return max_area