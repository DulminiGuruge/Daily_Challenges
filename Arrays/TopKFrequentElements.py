"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""
"""
Approach - 
To find the k most frequent elements in a given list, first create a dictionary to store the count 
of unique elements. Then, create an array(A) with a length of one more than the length of the input list. 
The index of the array represents the count of the occurrence of an element. Think indexes as the count of an 
element and append the values corresponding to the index which is equal to the count.
Next, create another array(B) to store the k frequent elements,
and loop through the created array(A) from reverse order to get the most frequent elements. 
Finally, add them to the newly created array (A).

Time complexity - O(n)
Space complexity

"""


def topKFrequent( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq_as_index = [[] for i in range(len(nums)+ 1)]

        for n in nums:
                count[n] = 1 + count.get(n,0)
        for n,c in count.items():
                freq_as_index[c].append(n)


        K_frequent_elements = []        

        for i in range(len(freq_as_index) - 1,0,-1):
                for n in freq_as_index[i]:
                        K_frequent_elements.append(n)
                        if len(K_frequent_elements) == k:
                                return K_frequent_elements




print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequent([1],1))
