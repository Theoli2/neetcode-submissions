class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum())
        lower = clean.lower()
        print(lower)
        for left_char, right_char in zip(lower, reversed(lower)):
            if (left_char != right_char):
                return False

        return True