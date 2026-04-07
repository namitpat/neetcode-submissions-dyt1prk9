class Solution:
    def isPalindrome(self, s: str) -> bool:
        isPalindrome=True
        clean = "".join(char.lower() for char in s if char.isalnum())
        n=len(clean)//2
        for i in range(n):
            if clean[i]==clean[len(clean)-i-1]:
                continue
            isPalindrome=False
        return isPalindrome
            
            

        