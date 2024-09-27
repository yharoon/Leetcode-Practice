'''

https://leetcode.com/problems/single-number-iii/description/

Given an integer array nums, in which exactly two 
elements appear only once and all the other elements 
appear exactly twice. Find the two elements that 
appear only once. You can return the answer in any 
order.

You must write an algorithm that runs in linear 
runtime complexity and uses only constant extra 
space.

---

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]

---

ideas;
    - if only 2 elements appear only once, then maybe
    we can have 2 pointers at the first 2 elements
    - if they are the same, make 1 of them the next
    available element, if they aren't check the next
    available element, if it matches one of the pointer
    elements, then move that one to the next available
    element and continue until we are at the end of the
    list.

'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        print(str(xor)+" xor")

        lowestSetBit = xor & -xor
        print(str(lowestSetBit)+" lsb")

        res = [0,0]
        for num in nums:
            print(str((lowestSetBit & num)) + " lsb & num")
            if (lowestSetBit & num) == 0:
                res[0] ^= num
                print(str(res[0])+ " res[0]")
            else:
                res[1] ^= num
                print(str(res[1])+ " res[1]")
        
        return res
    
sol = Solution()
arr = [2,1,2,3,4,1]
print(sol.singleNumber(arr))