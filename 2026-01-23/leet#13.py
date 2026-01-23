class Solution:
    def intToRoman(self, num: int) -> str:
        # Define all symbols from largest to smallest
        # We include the "subtractive" cases (900, 400, etc.) as their own symbols
        symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in symbols:
            # While the current number is bigger than the Roman value
            while num >= value:
                result.append(symbol) # Add the symbol
                num -= value          # Subtract the value
                
        return "".join(result)