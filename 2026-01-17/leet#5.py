class Solution:
    str = "PAYPALISHIRING"
    numRows = 4
    def convert(self, s: str, numRows: int) -> str:
        storage = [[None for _ in range(99)] for _ in range(numRows)]
        length = len(s)
        for i in range(length):
            storage[i][j] = str[i]
            if i == numRows - 1:
                j = j + 1
                i = 0

            return storage 