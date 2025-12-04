class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        while i < n1 or i < n2:
            if i < n1:
                merged.append(word1[i])
            if i < n2:
                merged.append(word2[i])
            i = i+1
        return "".join(merged)
