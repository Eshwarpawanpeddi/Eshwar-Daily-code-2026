class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        
        result = [""]
        
        for d in digits:
            temp = []
            for combination in result:
                for letter in phone_map[d]:
                    temp.append(combination + letter)
            result = temp
            
        return result