"""
Question -

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

"""
"""

Approach - We can use a hashset we can add values in O(1) and check for duplicates in O(1) but
    we have to sacrifice the space complexity. The memory of the hashset could be to a size of
    the input list. The runtime is higher in this approach than the next approach when the input contains 
    lesser elements

Time complexity - O(n)
Space complexity - O(n)


"""

def containsDuplicate(nums):
        hashset = set()

        for x in nums:
            if x in hashset:
                return True
            else:
                hashset.add(x)

        return False        

print(containsDuplicate([3,5,6,6,7]))

"""

Approach - When we sort the list,if there are any duplicates they will be adjacent. So,
    we only need to iterate throught the list once.
    eg: 2,1,3,4,1 when sorted 1,1,2,3,4
    This approach is better when the input has more elements.

Time complexity - O(n log n) when we use the sorting algorithm
Space complexity - O(1)


"""

def containsDuplicate(nums):
        nums.sort
        length = len(nums)
    
        for x in range(len(nums)):
              if x == length-1:
                    return False
              else:
                    if nums[x]==nums[x+1]:
                          return True
                     
                       

print(containsDuplicate([3,5,6,9,9]))