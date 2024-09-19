'''

https://leetcode.com/problems/assign-ss/description/

Assume you are an awesome parent and want to give 
your children some ss. But, you should give 
each child at most one s.

Each child i has a g factor g[i], which is the 
minimum size of a s that the child will be 
content with; and each s j has a size s[j]. 
If s[j] >= g[i], we can assign the s j to the 
child i, and the child i will be content. Your goal 
is to maximize the number of your content children 
and output the maximum number.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 ss. 
The g factors of 3 children are 1, 2, 3. 
And even though you have 2 ss, since their 
size is both 1, you could only make the child whose 
g factor is 1 content.
You need to output 1.

Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 ss. 
The g factors of 2 children are 1, 2. 
You have 3 ss and their sizes are big enough 
to gratify all of the children, 
You need to output 2.

Constraints:

    1 <= g.length <= 3 * 10^4
    0 <= s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1

---

ideas;
    - we could try a gy algorithm that takes
    the largest s val and the largest g val
    which is equal to or smaller than the s
    val and then iterate to count how many times
    we can do that, but then we probably need
    to do it iteratively instead of recursively.
    - we could also use a 2 pointers approach,
    by starting the pointers at the end and
    comparing the g val at p1 to the s val
    at p2, we would need to pre sort the lists first
    for this to work, and i dont know if they are
    already sorted so ill just sort in case
    - if we do it this way, we must move the pointers
    down, if the g is larger than the size, we
    move down the g pointer, if g[p_g] <= c[p_c]
    ,then we decrement both and add 1 to the satisfied
    count
    - we keep doing this until one or both reach the
    end of the line (0)

'''

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        pointer_g = (len(g)-1)
        pointer_s = (len(s)-1)
        satisfied = 0

        while (pointer_s > -1) and (pointer_g > -1):
            if g[pointer_g] > s[pointer_s]:
                pointer_g -= 1
            elif g[pointer_g] <= s[pointer_s]:
                pointer_s -= 1
                pointer_g -= 1
                satisfied += 1
        
        return satisfied