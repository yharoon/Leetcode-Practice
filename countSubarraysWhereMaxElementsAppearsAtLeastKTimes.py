'''

https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/

You are given an integer array nums and a positive 
integer k.

Return the number of subarrays where the maximum 
element of nums appears at least k times in that 
subarray.

A subarray is a contiguous sequence of elements 
within an array.

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the 
element 3 at least 2 times are: [1,3,2,3], 
[1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at 
least 3 times.

---

ideas;
    - topics say sliding window, so we can probably
    do this
    - we start with the largest sliding window
    and then decrease the window size and go again
    but i feel like this is going to be inefficient
    - need to be count(element)>=k &&
    element = max(sub_arr.elements)
'''

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        window_size = len(nums)
        max_element = max(nums)
        i = 0
        j = i + window_size

        found = 0

        while (window_size >= (k-1)):
            print("current window_size: "+str(window_size))
            while (j < len(nums)):
                print("current search space: "+str(nums[i:j+1]))
                print("current i: "+str(i))
                print("current j: "+str(j))
                if (nums[i:j+1].count(max_element) >= k):
                    found += 1
                    print("found: "+str(nums[i:j+1]))
                i+=1
                j+=1
            window_size -= 1
            i = 0
            j = i + window_size
        
        return found
    
sol = Solution()
nums = [1,3,2,3,3]
print(sol.countSubarrays(nums,2))