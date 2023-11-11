"""
Question - 

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


"""

"""
Method 1

Create two dictioneries containing each character as the key 
and the count of the character in the string as the value.

Time complexity - O(s+t) because we have to iterate through both s and t
Space Complexity - O(s+t) to create two hashmaps with length s and t 
"""

from collections import Counter


def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        t_count,s_count = {},{}

        for x in range(len(s)):
            t_count[t[x]] = 1 + t_count.get(t[x],0)
            s_count[s[x]] = 1 + s_count.get(s[x],0)

        for c in s_count.keys():
            
               if s_count[c] != t_count.get(c,0):
                      return False
        return True          



print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))


"""
Method 2

This has the same time complexity and space complexity as the method 2
"""
def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))  


"""
How to reduce the space complexity.
We can sort the characters in the string and compare. The time complexity depends on the 
sorting algorithm used.

Space complexity = O(1)

"""
def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))  