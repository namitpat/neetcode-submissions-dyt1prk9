class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome=True
        clean = "".join(char.lower() for char in s if char.isalnum())
        n=len(clean)//2
        for i in range(n):
            if clean[i]==clean[len(clean)-i-1]:
                continue
            isPalindrome=False
        if isPalindrome==False:
            for i in range(len(s)):
                newS=s[:i]+s[i+1:]
                if newS==newS[::-1]:
                    return True

        return isPalindrome
        