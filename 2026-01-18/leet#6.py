class Solution:
    def reverse(self, x: int) -> int:
        my_list = list(x)
        if len(my_list) > 0:
            if my_list[0] == '-':
                symbol = "-"
                my_list.pop(0)
            my_list = my_list[::-1]
            if my_list[0] =="0":
                my_list.pop(0)
        final_ans = symbol + my_list
        return final_ans