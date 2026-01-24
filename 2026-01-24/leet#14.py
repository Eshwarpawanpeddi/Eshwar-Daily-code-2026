class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        while 1<= len(strs) <= 200 and all(1 <= len(s) <= 200 for s in strs):
            longest_suffix = []

            for i in range(len(strs)):
                if len(strs[i]) < j:
                    strs[i] = strs[i].ljust(j, ' ')

            for words in strs:
                if words[i][j] == words[i+1][j] == words[i+2][j]:
                    longest_suffix.append(words[i][j])
                    j += 1
                else:
                    break
            return ''.join(longest_suffix)