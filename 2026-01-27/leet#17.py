class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '1':'','2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' ,'0': ' '
        }
        
        result = []
        
        diglist = digits.split()

        for nums in diglist:
            temp = ['']
            for d in nums:
                letters = phone_map[d]
                new_temp = []
                for prefix in temp:
                    for letter in letters:
                        new_temp.append(prefix + letter)
                temp = new_temp
            result.extend(temp)
            