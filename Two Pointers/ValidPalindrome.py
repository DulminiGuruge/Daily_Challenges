"""

Question -
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

"""
Method 1
Time complexity - O(n)
Space complexity - O(n)
"""
def isPalindrome( s):
        """
        :type s: str
        :rtype: bool
        """
        word = ""
        for c in s:
            if c.isalnum():
                word += c.lower()
        return word == word[::-1]                
                

print(isPalindrome("A man, a plan, a canal: Panama"))  
print(isPalindrome("race a car"))      
print(isPalindrome(" "))

"""
Method 2 -
Using Two pointers
We compare left most character with the right most character and if they are equal then
go to the next left most and right most characters and compare.Do this until the the pointers 
are in the middle or unitil the left pointer passes the right pointer.

Time complexity - O(n) because we iterate through the string
Space complexity - O(1) we don't create another array excluding non alpha numeric characters
"""

def isPalindrome2( s):
        """
        :type s: str
        :rtype: bool
        """
        left,right = 0, len(s)-1

        while left<right:
              #to ignore non alphanumeric characters and to increment the point 
              # to the next character
              while left< right and not alphaNum(s[left]):
                    left += 1

              while right > left and not alphaNum(s[right]):
                    right -= 1

              if s[left].lower() != s[right].lower():
                    return False   

              left,right = left+1,right-1   
        return True


def alphaNum(c):
    return ((ord('A')<= ord(c)<=ord('Z')) or
                      (ord('a')<= ord(c)<=ord('z')) or
                      (ord('0')<= ord(c)<=ord('9')))



print("")
print(isPalindrome2("A man, a plan, a canal: Panama"))  
print(isPalindrome2("race a car"))      
print(isPalindrome2(" "))


