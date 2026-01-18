class Solution:
    def reverse(self, x: int) -> int:
        my_list = list(str(x))
        
        symbol = ""
        
        if len(my_list) > 0: 
            if my_list[0] == '-':
                symbol = "-"
                my_list.pop(0)
            my_list = my_list[::-1]
            final_str = symbol + "".join(my_list)
            result = int(final_str)
            if result < -2**31 or result > 2**31 - 1:
                return 0
                
            return result