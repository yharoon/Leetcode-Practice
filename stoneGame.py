'''

https://leetcode.com/problems/stone-game-v/

There are several stones arranged in a row, and 
each stone has an associated value which is an 
integer given in the array stoneValue.

In each round of the game, Alice divides the row 
into two non-empty rows (i.e. left row and right row)
,then Bob calculates the value of each row which is
the sum of the values of all the stones in this row.
Bob throws away the row which has the maximum value, 
and Alice's score increases by the value of the 
remaining row. If the value of the two rows are 
equal, Bob lets Alice decide which row will be 
thrown away. The next round starts with the remaining 
row.

The game ends when there is only one stone remaining.
Alice's is initially zero.

Return the maximum score that Alice can obtain.

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the 
row to [6,2,3], [4,5,5]. The left row has the value 
11 and the right row has value 14. Bob throws away 
the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], 
[2,3]. This time Bob throws away the left row and
Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide 
the row which is [2], [3]. Bob throws away the right 
row and Alice's score is now 18 (16 + 2). The game 
ends because only one stone is remaining in the row.

Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28

Example 3:

Input: stoneValue = [4]
Output: 0

'''

class Solution(object):
    def stoneGameV(self, stoneValue):
        sz = len(stoneValue)
        dp, maxScore = [[0] * sz for _ in range(sz)], [[0] * sz for _ in range(sz)]
        for i in range(sz):
            maxScore[i][i] = stoneValue[i]
        for j in range(1, sz):
            mid, sm, rightHalf = j, stoneValue[j], 0
            for i in range(j - 1, -1, -1):
                sm += stoneValue[i]
                while (rightHalf + stoneValue[mid]) * 2 <= sm:
                    rightHalf += stoneValue[mid]
                    mid -= 1
                dp[i][j] = maxScore[i][mid] if rightHalf * 2 == sm else (0 if mid == i else maxScore[i][mid - 1])
                dp[i][j] = max(dp[i][j], 0 if mid == j else maxScore[j][mid + 1])
                maxScore[i][j] = max(maxScore[i][j - 1], dp[i][j] + sm)
                maxScore[j][i] = max(maxScore[j][i + 1], dp[i][j] + sm)
        return dp[0][sz - 1]


sol = Solution()

arr = [10,9,8,7,6,5,4,3,2,1]
print(sol.stoneGameV(arr))