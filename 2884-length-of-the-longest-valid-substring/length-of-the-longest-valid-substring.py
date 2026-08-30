from typing import List

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        n = len(word)
        max_length = 0
        max_valid_right = n - 1
        
        for left in range(n - 1, -1, -1):
            for right in range(left, min(left + 10, max_valid_right + 1)):
                if word[left : right + 1] in forbidden_set:
                    max_valid_right = right - 1
                    break
            
            current_len = max_valid_right - left + 1
            if current_len > max_length:
                max_length = current_len
            
        return max_length
