class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        answer = []
        while i < len(s) and s[i].isdigit():
            answer.append(s[i])
            i += 1
        if not answer:
            return 0
        value = int("".join(answer)) * sign
        low = -2**31
        high = 2**31 - 1
        
        if value < low: return low
        if value > high: return high
        
        return value