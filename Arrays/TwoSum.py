"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

"""

Frist we need to cretae a hashmap to add the values in the array. Keys are the 
element in the array and the value is the index of the element in the array.
Then, iterate through eachelement x in the array and see whether
the (target - x) is in the hashmap, if exissts return the value of the key and the index of the current element x.

Time complexity = O(n)
Space complexity = O(n)

"""

def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for ind,val in enumerate(nums):
            difference = target - val
            if difference in hashmap:
                  return [hashmap[difference],ind]
            
            hashmap[val] = ind
                
        

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
