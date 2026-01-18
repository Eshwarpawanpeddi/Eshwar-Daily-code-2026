class Solution:
    def reverse(self, x: int) -> int:
        my_list = [x]
        if len(my_list) > 0:
            if my_list[0] == '-':
                symbol = "-"
                my_list.pop(0)
            else:
                symbol = ""
            my_list = my_list[::-1]
            if my_list[0] =="0":
                my_list.pop(0)
            final_ans = []
            final_ans.append(symbol)
            final_ans.join(my_list)]
        return final_ans