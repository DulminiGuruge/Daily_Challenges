
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.
"""
"""
Approach - We use character count which consist of 26 characters from a..z.


Time complexity - O(m.n)
Space complexity - O(m.n)
"""

from collections import defaultdict


def groupAnagrams( strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        character_tuples_dict = defaultdict(list)   
        #Defaultdict is a container like dictionaries present in 
        # the module collections. Defaultdict is a sub-class of 
        # the dictionary class that returns a dictionary-like object. 
        # The functionality of both dictionaries and defaultdict are almost 
        # same except for the fact that defaultdict never raises a KeyError. 
        # It provides a default value for the key that does not exists. 

        for word in strs:
                count = [0] * 26 # list to store ascii value from a...z

                for letter in word:
                        count[ord(letter)- ord("a")]+=1

                character_tuples_dict[tuple(count)].append(word)

        print(count)
        print("-----")
        print(character_tuples_dict)
        return character_tuples_dict.values()

                


                        



print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]) )
print("\n")

print(groupAnagrams([""]))
print("\n")

print(groupAnagrams(["a"]))       