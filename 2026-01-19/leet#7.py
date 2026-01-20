class Solution:
    def myAtoi(self, s: str) -> int:
        words = list(s)
        answer = []
        for char in words[:]:
            if char == ' ':
                words.remove(char)
        for char in words[:]:
            if char.isdigit() == True:
                answer.append(char)
            elif char.isalpha() == True or char in ['+', '-', '.']:     
                break
        str_conv = ''.join(answer)
        return int(str_conv)
    