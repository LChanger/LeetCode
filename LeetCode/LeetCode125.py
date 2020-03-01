# 题目描述：Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Note: For the purpose of this problem, we define empty string as valid palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:return False
        s=s.upper()
        low=0
        high=len(s)-1
        while low<high:
            if not s[low].isalpha():
                low+=1
                continue
            if not s[high].isalpha():
                high-=1
                continue
            if s[low]!=s[high]:
                return False
            low+=1
            high-=1
        return True
            
        
        
t1="A man, a plan, a canal: Panama"
t = Solution()
print(t.isPalindrome(t1))