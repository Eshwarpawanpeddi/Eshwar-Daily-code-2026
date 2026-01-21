class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # memo stores results we've already calculated to save time
        memo = {}

        def dp(i, j):
            # If we've seen this pair of indices before, return the saved result
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: if we reach the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check if the current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handling the '*'
            if j + 1 < len(p) and p[j+1] == '*':
                # Decision 1: Skip the '*' (match 0 times)
                # Decision 2: Use the '*' (if first_match is true, move s pointer i+1)
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # No '*', so just move both pointers if they match
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)