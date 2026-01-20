class Solution:
    def myAtoi(self, s: str) -> int:
        words = list(s)
        for char in words[:]:
            if char == ' ':
                words.remove(char)
        
