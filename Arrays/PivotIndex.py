"""
Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 
Approach -
Let's say we knew S as the sum of the numbers, and we are at index i. If we knew the sum of numbers leftsum 
that are to the left of index i, then the other sum to the right of the index would just be S - nums[i] - leftsum.
As such, we only need to know about leftsum to check whether an index is a pivot index in constant time.
Let's do that: as we iterate through candidate indexes i, we will maintain the correct value of leftsum.

Time complexity - O(n) length of nums
Space complexity - O(1) space used by left_sum and total

"""

def pivotIndex( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for index,val in enumerate(nums):
            if left_sum ==(total - val - left_sum):
                return index
            
            left_sum += val
        return -1    




print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))
