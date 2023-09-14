'''
Example: s1: 'horse'
         s2: 'ros'

Case1: Inserting a Character

Now if we have to match the strings by insertions, what would we do?: 

We would have placed an ‘s’ at index 5 of S1.
Suppose i now point to s at index 5 of S1 and j points are already pointing to s at index j of S2.
Now, we hit the condition, where characters do match. (as mentioned in case 1).
Therefore, we will decrement i and j by 1. They will now point to index 4 and 1 respectively.

Now, the number of operations we did were only 1 (inserting s at index 5) but do we need to really insert the ‘s’ at index 5 and modify the string? The answer is simply NO. As we see that inserting a character (here ‘s’ at index 5), we will eventually get to the third step. So we can just return 1+ f(i,j-1) as i remains there only after insertion and j decrements by 1. We can say that we have hypothetically inserted character s.

Case 2: Deleting a character 

Consider the same example,

We can simply delete the character at index 4 and check from the next index.

Now, j remains at its original index and we decrement i by 1. We perform 1 operation, therefore we will recursively call 1+f(i-1,j).

Case3: Replacing a character 

Consider the same example,


If we replace the character ‘e’ at index 4 of S1 with ‘s’, we have matched both the characters ourselves. We again hit the case of character matching, therefore we decrement both i and j by 1. As the number of operations performed is 1, we will return 1+f(i-1,j-1).

To summarise, these are the three choices we have in case characters don’t match:

return 1+f(i-1,j) // Insertion of character.
return 1+f(i,j-1) // Deletion of character.
return 1+f(i-1,j-1) // Replacement of character.
'''

#Recursion 
#Time Complexity: O(2^(m+n))
#Space Complexity: O(m+n)
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(i,j):
            if i==0:
                return j
            if j==0:
                return i
            if word1[i-1]==word2[j-1]:
                return solve(i-1,j-1)
            else:
                return 1 + min(solve(i,j-1),solve(i-1,j),solve(i-1,j-1))
        m,n=len(word1),len(word2)
        return solve(m,n)
    
#Memoization (Top-Down)
#Time Complexity: O(m*n)
#Space Complexity: O(m+n) + O(m*n)
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(i,j):
            if i==0:
                return j
            if j==0:
                return i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i-1]==word2[j-1]:
                dp[i][j]=solve(i-1,j-1)
                return dp[i][j]
            else:
                dp[i][j]=1 + min(solve(i,j-1),solve(i-1,j),solve(i-1,j-1))
                return dp[i][j]
        m,n=len(word1),len(word2)
        dp=[[-1 for j in range(n+1)] for i in range(m+1)]
        return solve(m,n)
    
class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[m][n]
    
#Space Optimization
#Time Complexity: O(m*n)
#Space Complexity: O(n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        prev=[0]*(n+1)
        curr=[0]*(n+1)
        for j in range(n+1):
            prev[j]=j
        for i in range(1,m+1):
            curr[0]=i
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j-1], prev[j], curr[j-1])
            prev=curr[:]
        return prev[n]
    

# https://zhuanlan.zhihu.com/p/553078167
# 动态规划三部曲  1)dp数组含义  2)初始值  3)状态转移方程
# dp[i][j]定义为 word1前i个字符转换到word2前j个字符所需的最少操作数
#   | '' | r | o | s 
# ''| 0  | 1 | 2 | 3
# h | 1  | 
# o | 2  |
# r | 3  |
# s | 4  |
# e | 5  |
# dp[0][j]的含义: 从''转换为'',r,ro,ros所需的最少操作数
# dp[i][0]的含义: 从'',h,ho,hor,hors,horse转换为''所需的最少操作数
# dp[i][j] = dp[i-1][j-1] if word1[i-1]==word2[j-1] else min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
def editDistance(word1, word2):
    m,n = len(word1),len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = i if j==0 else j
            else:
                dp[i][j] = dp[i-1][j-1] if word1[i-1]==word2[j-1] else min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
    return dp[m][n]


from functools import lru_cache
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)

    @lru_cache(None)
    def dp(i,j):
        if i>=m: return n-j
        if j>=n: return m-i
        if word1[i] == word2[j]: return dp(i+1, j+1)
        return min(dp(i,j+1), dp(i+1,j), dp(i+1,j+1)) + 1
    
    return dp(0,0)