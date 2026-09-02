class Solution:
    def reverseWords(self, s: str) -> str:
        # Split automatically handles multiple spaces and strips whitespaces
        words = s.split()
        
        # Reverse the list of words and join them with a single space
        return " ".join(words[::-1])
